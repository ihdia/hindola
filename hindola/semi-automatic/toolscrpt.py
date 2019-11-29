import torch
import json
import cv2
import json
import numpy as np
import math
import argparse
import torch
from edgeonlyy import Model
import ConcaveHull as ch
from torch.utils.data import DataLoader
import operator
import torch.nn as nn
import socket
import selectors
import types
import time
from skimage import io
from collections import OrderedDict
from simplification.cutil import simplify_coords

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if torch.cuda.is_available():
	print("!!!!!!got cuda!!!!!!!")
else:
	print("!!!!!!!!!!!!no cuda!!!!!!!!!!!!")

def uniformsample_batch(batch, num):
	final = []
	for i in batch:
		i1 = np.asarray(i).astype(int)
		a = uniformsample(i1, num)
		a = torch.from_numpy(a)
		a = a.long()
		final.append(a)
	return final

def uniformsample(pgtnp_px2, newpnum):
	pnum, cnum = pgtnp_px2.shape
	assert cnum == 2

	idxnext_p = (np.arange(pnum, dtype=np.int32) + 1) % pnum
	pgtnext_px2 = pgtnp_px2[idxnext_p]
	edgelen_p = np.sqrt(np.sum((pgtnext_px2 - pgtnp_px2) ** 2, axis=1))
	edgeidxsort_p = np.argsort(edgelen_p)

	# two cases
	# we need to remove gt points
	# we simply remove shortest paths
	if pnum > newpnum:
		edgeidxkeep_k = edgeidxsort_p[pnum - newpnum:]
		edgeidxsort_k = np.sort(edgeidxkeep_k)
		pgtnp_kx2 = pgtnp_px2[edgeidxsort_k]
		assert pgtnp_kx2.shape[0] == newpnum
		return pgtnp_kx2
	# we need to add gt points
	# we simply add it uniformly
	else:
		edgenum = np.round(edgelen_p * newpnum / np.sum(edgelen_p)).astype(np.int32)
		for i in range(pnum):
			if edgenum[i] == 0:
				edgenum[i] = 1

		# after round, it may has 1 or 2 mismatch
		edgenumsum = np.sum(edgenum)
		if edgenumsum != newpnum:

			if edgenumsum > newpnum:

				id = -1
				passnum = edgenumsum - newpnum
				while passnum > 0:
					edgeid = edgeidxsort_p[id]
					if edgenum[edgeid] > passnum:
						edgenum[edgeid] -= passnum
						passnum -= passnum
					else:
						passnum -= edgenum[edgeid] - 1
						edgenum[edgeid] -= edgenum[edgeid] - 1
						id -= 1
			else:
				id = -1
				edgeid = edgeidxsort_p[id]
				edgenum[edgeid] += newpnum - edgenumsum

		assert np.sum(edgenum) == newpnum

		psample = []
		for i in range(pnum):
			pb_1x2 = pgtnp_px2[i:i + 1]
			pe_1x2 = pgtnext_px2[i:i + 1]

			pnewnum = edgenum[i]
			wnp_kx1 = np.arange(edgenum[i], dtype=np.float32).reshape(-1, 1) / edgenum[i];

			pmids = pb_1x2 * (1 - wnp_kx1) + pe_1x2 * wnp_kx1
			psample.append(pmids)

		psamplenp = np.concatenate(psample, axis=0)
		return psamplenp

def get_hull(edge_logits):
	test = edge_logits
	test_0 = test[:, :]
	test_1 = test[:, :]

	


	# for i in range(len(test_0)):
	#     for j in range(len(test_0[0])):
	#         if test_0[i][j] > 0.7:
	#             test_1[i][j] = 1
	#         else:
	#             test_1[i][j] = 0
	points_pred = []

	for i in range(len(test_1)):
		for j in range(len(test_1[0])):
			if test_1[i][j] > 0:
				points_pred.append([i + 1, j + 1])

	points_pred = np.asarray(points_pred)

	hull, error_val = ch.concaveHull(points_pred, 3)
	return hull, error_val

def convert_hull_to_cv(hull, w, h):

	original_hull = []

	# w = bbox[2] + 20
	# h = bbox[3]

	for i in hull:
		original_hull.append([int((i[1]-5) * w / 80), int((i[0]-2) * h / 20)])
	return original_hull

model_path = '/semi-automatic/LinesBest.pth'
model = Model(256, 960, 3).to(device)
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
print("Let's use", torch.cuda.device_count(), "GPUs!")
# dim = 0 [20, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
# model = nn.DataParallel(model)

# state_dict = torch.load(model_path)
if (torch.cuda.device_count() < 1):
	state_dict = torch.load(model_path, map_location = lambda storage, loc: storage)
	new_state_dict = OrderedDict()
	for k, v in state_dict["gcn_state_dict"].items():
		name = k[7:]
		new_state_dict[name] = v
	model.load_state_dict(new_state_dict)

else:
	model = nn.DataParallel(model)
	state_dict = torch.load(model_path)
	model.load_state_dict(state_dict["gcn_state_dict"])

model.to(device)

def get_edge(i_url,bbox):

	err_val = 0
	img = cv2.imread(i_url)
	#cv2.cvtColor(img, img, cv2.COLOR_RGB2BGR)

	x0 = max(int(bbox[0]),0)
	y0 = max(int(bbox[1]),0)
	w = max(int(bbox[2]),0)
	h = max(int(bbox[3]),0)

	img = img[y0:y0+h,x0:x0+w]

	# img= cv2.copyMakeBorder(img,0,0,10,10,cv2.BORDER_REPLICATE)
	img = cv2.resize(img, (256, 960))
	img = torch.from_numpy(img)


	# img = torch.cat(img)
	try:
		img = img.view(-1, 256, 960, 3)
	except:
		err_val = 1
		return i_url, [], [], err_val

	img = torch.transpose(img, 1, 3)
	img = torch.transpose(img, 2, 3)
	img = img.float()

	edge_logits, tg2, class_prob = model(img.to(device))
	edge_logits = torch.sigmoid(edge_logits)

	edge_logits = edge_logits[0,0,:,:].cpu().detach().numpy()
	# print(len(edge_logits))
	arrs1 = np.zeros((24, 90), np.uint8)

	for j in range(len(edge_logits)):
		for k in range((len(edge_logits[j]))):
			j1 = math.floor(j)
			k1 = math.floor(k)
			if edge_logits[j][k]>0.6:
				arrs1[j1+2][k1+5]= 255


	borders = np.zeros((24, 90), np.uint8)
	kernel5 = np.ones((3,3),np.uint8)

	arrs1 = cv2.morphologyEx(arrs1, cv2.MORPH_CLOSE, kernel5)
	
	contours, hierarchy = cv2.findContours(arrs1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(borders, contours, -1, 255, 1)

	arrs1 = np.zeros((24, 90), np.float32)
	for j in range(len(borders)):
		for k in range((len(borders[j]))):
			j1 = math.floor(j)
			k1 = math.floor(k)
			if borders[j][k] > 180:
				arrs1[j1][k1]= 1.0

	arrs1 = torch.from_numpy(arrs1)
	hull, err_val = get_hull(arrs1)
	if (err_val == 1):
		return i_url, [], [], err_val

	hull = np.asarray(hull)

	hull = simplify_coords(hull, 0.1)

	hull = hull.tolist()


	original_hull = convert_hull_to_cv(hull, w, h)

	total_points = 200
	# original_hull = uniformsample(np.asarray(original_hull), total_points).astype(int)
	original_hull = np.asarray(original_hull).astype(int)
	all_points_x = np.int32((original_hull[:,0] + x0)).tolist()
	all_points_y = np.int32((original_hull[:,1] + y0)).tolist()

	# all_points_x = simplify_coords_vw(all_points_x, 30.0)
	# all_points_y = simplify_coords_vw(all_points_y, 30.0)

	return i_url, all_points_x, all_points_y, err_val

# if __name__ == '__main__':
#     x, y = get_edge("./Andros332.jpg", [28,349,150,25])
#     print(x,y)








HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 40000       # Port to listen on (non-privileged ports are > 1023)


sel = selectors.DefaultSelector()

def accept_wrapper(sock):
	conn, addr = sock.accept()  # Should be ready to read
	print('accepted connection from', addr)
	conn.setblocking(False)
	data = types.SimpleNamespace(addr=addr, inb='', outb='')
	events = selectors.EVENT_READ | selectors.EVENT_WRITE
	sel.register(conn, events, data=data)

def service_connection(key, mask):
	sock = key.fileobj
	data = key.data
	if mask & selectors.EVENT_READ:
		recv_data = sock.recv(500024)  # Should be ready to read
		if recv_data:
			data.outb += recv_data.decode('utf-8')
			input_json = json.loads(data.outb)
			fileurl, all_points_x, all_points_y, err_val = get_edge(input_json['fileurl'], [input_json['x'], input_json['y'], input_json['width'], input_json['height']])
			output_json = {}
			output_json['all_points_x'] = all_points_x
			output_json['all_points_y'] = all_points_y
			output_json['flag'] = 2
			output_json['url'] = fileurl
			output_json['error'] = err_val
			data.inb += json.dumps(output_json)
			recv_data = ''
			
		else:
			print('closing connection to', data.addr)
			sel.unregister(sock)
			sock.close()
	if mask & selectors.EVENT_WRITE:
		if data.outb:
	#		queue_entry = {'args': data.outb, 'client': sock, 'mask': mask}
	#		q.enqueue(queue_entry)
	#		if q.is_empty() == False:
	#			print(json.loads((q.items[-1])['args']))
	#			#print(q.items[-1])
	#			q.dequeue()
			print("sending json back")
			#sent = sock.sendall((data.outb).encode('utf-8'))  # Should be ready to write
			sent = sock.sendall((data.inb).encode('utf-8'))  # Should be ready to write
			data.outb = ''
			data.inb = ''


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	s.setblocking(False)
	sel.register(s, selectors.EVENT_READ, data=None)

	while True:
		events = sel.select(timeout=None)
		#print(q.items)
		for key, mask in events:
			if key.data is None:
				accept_wrapper(key.fileobj)
			else:
				service_connection(key, mask)
