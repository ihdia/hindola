import cv2
import os
import sys
import random
import math
import re
import time
import socket
import selectors
import types
import json
import numpy as np
import tensorflow as tf
from wrapt_timeout_decorator import *
# import timeout_decorator
# print(tf.__version__)
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from keras.models import load_model
import keras.backend as K
ROOT_DIR1 = os.path.abspath("/")
print(ROOT_DIR1)
ROOT_DIR = os.path.abspath("/Instance-segmentation-master")
print(ROOT_DIR)
# ROOT_DIR = os.path.abspath("../../")
# print(ROOT_DIR,"ROOT")
sys.path.append(ROOT_DIR)
# print(sys.path)
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log
from main.doc import train
from PIL import Image
#edited divija.p
from app1 import *
# from perimeter import arr,count
import urllib.request
from skimage import io
from shapely.geometry import Polygon
config = train.Config()
DOCDATA = ROOT_DIR+"datasets/doc"
OUTPUTPATH=  ROOT_DIR+"/main/doc/static/images/2.jpg"
IMG1PATH= ROOT_DIR+"/main/doc/static/images/1.jpg"
import argparse
parser = argparse.ArgumentParser()
MODEL_DIR = os.path.join(ROOT_DIR, "logs")
config = train.Config()
MAIN_DIR = os.path.join(ROOT_DIR, "datasets/doc")


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# filename =" "





# if __name__ == '__main__':

11
	# arr1 = np.zeros(11)
	# count1 = np.zeros(11)
# print (Polygon([[0,0], [4,0], [2,4]]).length,"length")
# 
	# config = train.Config()
	# DOCDATA = ROOT_DIR+"datasets/doc"
	# OUTPUTPATH=  ROOT_DIR+"/main/doc/static/images/2.jpg"
	# IMG1PATH= ROOT_DIR+"/main/doc/static/images/1.jpg"
#edited divija.p

#edited divija.p
# with urllib.request.urlopen(filepath) as url:

#     s = url.read()
#     # I'm guessing this would output the html source code ?
#     print(s)

# arguments 
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-c","--filepath",help="filepath for JSON")
# args = vars(parser.parse_args())
# print(args['filepath'])
# #edited divija.p
# filepath= args['filepath']
# filename=str(filepath)

#edited divija.p
def image_url_to_numpy_array_skimage(url,format=None):
    from skimage import io
    image = io.imread(url)
    image = np.asarray(image, dtype="uint8")
    if format=='BGR' :
        ## return BGR format array
        return image[...,[2,1,0]]
    return image



# image=image_url_to_numpy_array_skimage(url=filepath)

# # image = Image.open(urllib.request.urlopen(filepath))
# # # resp = urllib.request.urlopen(filepath)
# # # image = np.asarray(bytearray(resp.read()), dtype="uint8")
# # # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
# img=image
# print(type(img),"p")
# print(img.shape,"size")
# # cv2.imshow('ImageWindow', img)
# # cv2.waitKey()
# print("uuu")
# 
# added  divija.p
class InferenceConfig(config.__class__):
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1
	IMAGE_RESIZE_MODE = "square"
	DETECTION_MIN_CONFIDENCE = 0.6
	DETECTION_NMS_THRESHOLD = 0.3
	PRE_NMS_LIMIT = 12000
	RPN_ANCHOR_SCALES = (8,32,64,256,1024)
	RPN_ANCHOR_RATIOS = [1,3,10]

	POST_NMS_ROIS_INFERENCE = 12000
	
	'''
	
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1
	IMAGE_RESIZE_MODE = "square"
	DETECTION_MIN_CONFIDENCE = 0.3
	DETECTION_NMS_THRESHOLD = 0.3
	PRE_NMS_LIMIT = 12000
	RPN_ANCHOR_SCALES = (8,32,64,256,1024)
	RPN_ANCHOR_RATIOS = [1,3,10]

	POST_NMS_ROIS_INFERENCE = 12000
	'''
def load_model():
	config = InferenceConfig()
	DEVICE = "/cpu:0"  # /cpu:0 or /gpu:0
	TEST_MODE = "inference"
	global dataset
	dataset = train.Dataset()

	# changed divija
	dataset.load_data(MAIN_DIR, "val")
	dataset.prepare()

	print("Images: {}\nClasses: {}".format(len(dataset.image_ids), dataset.class_names))
	global model
	with tf.device(DEVICE):
		model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR,
							  config=config)
	
	ROOT_DIR = os.path.abspath("/Instance-segmentation-master")
	weights_path= "/pretrained_model_indiscapes.h5"
	# weights_path = "http://localhost:8000/pretrained_model_indiscapes.h5"
	# weights_path = "https://drive.google.com/file/d/1TFUEjo4D7een7C7fGJV-xrU1cKi_hFeO/view"
	print(weights_path,"weights_path")
	print(ROOT_DIR,"ROOT_DIR")
	print("Loading weights ", weights_path)
	model.load_weights(weights_path, by_name=True)
	global graph
	graph = tf.get_default_graph()



# 
# if __name__ == '__main__':
# @timeout(5,use_signals=False)
def modeltest1(filepath,i,name):

	arr1 = np.zeros(11)
	count1 = np.zeros(11)
	name = name
	# parser.add_argument("-c","--filepath",help="filepath for JSON")
	# args = vars(parser.parse_args())
	# print(args['filepath'])
	#edited divija.p
	# filepath= args['filepath']
	filename=str(filepath)
	filepath=filepath

	image=image_url_to_numpy_array_skimage(url=filepath)

	# image = Image.open(urllib.request.urlopen(filepath))
	# # resp = urllib.request.urlopen(filepath)
	# # image = np.asarray(bytearray(resp.read()), dtype="uint8")
	# # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	img=image
	# print(type(img),"p")
	# print(img.shape,"size")
	# cv2.imshow('ImageWindow', img)
	# cv2.waitKey()
	# print("uuu")

	load_model()
	# app.run('0.0.0.0', debug=True)
	with graph.as_default(): 
		# print(img.shape,"shape in __name__")
		out = runtest(img,model,dataset,filename,name)

	if(not out):
		out = {}
		out['error'] = 1
	else:
		out = json.loads(out)
		out['error'] = 0
	out['flag'] = 1
	i[0]=2
	print(i[0],"i from the other side")
	return out

def get_ax(rows=1, cols=1, size=16):
	_, ax = plt.subplots(rows, cols, figsize=(size*cols, size*rows))
	return ax
def runtest(img,model,dataset,filename,name):

	import json
	# image=img
	image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	# print(image.shape,"image shape1")
	image,_,scale,scale1,padding,_=utils.resize_image(image,min_dim=256, max_dim=1024)
	# print(scale, "  ", scale1)
	results = model.detect([image], verbose=1)
	# print("iii")
	ax = get_ax(1)
	# print("iiii")
	r = results[0]
	# print(image.shape,"image shape before contours")
	ccc,contours=visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
	                            dataset.class_names, r['scores'], ax=ax,
	                            title="Predictions",show_bbox=False,show_mask=True)
	# print(len(contours))
	arr = np.array(contours)
	# print(arr[0][0][0][0],"shape")

	# print(contours[0][0],"contours")
	# print(contours[0])
	cls=r['class_ids']
	classes = ['Background','Hole(Virtual)','Hole(Physical)','Character Line Segment',
	           'Physical Degradation','Page Boundary','Character Component','Picture',
	           'Decorator','Library Marker','Boundary Line']

	strt="""
	{
	  "_via_settings": {
	    "ui": {
	      "annotation_editor_height": 30,
	      "annotation_editor_fontsize": 0.6000000000000001,
	      "leftsidebar_width": 18,
	      "image_grid": {
	        "img_height": 80,
	        "rshape_fill": "none",
	        "rshape_fill_opacity": 0.3,
	        "rshape_stroke": "yellow",
	        "rshape_stroke_width": 2,
	        "show_region_shape": true,
	        "show_image_policy": "all"
	      },
	      "image": {
	        "region_label": "region_id",
	        "region_label_font": "10px Sans"
	      }
	    },
	    "core": {
	      "buffer_size": 18,
	      "filepath": {},
	      "default_filepath": ""
	    },
	    "project": {
	      "name": "corrected_3"
	    }
	  },
	  "_via_img_metadata": {
	    "": {
	      "filename": \""""+str(filename)+"""\",
	      "size": -1,
	      "regions": [
	"""

	end="""
	],
	      "file_attributes": {}
	    }
	  },
	  "_via_attributes": {
	    "region": {
	      "Spatial Annotation": {
	        "type": "dropdown",
	        "description": "",
	        "options": {
	          "Hole(Virtual)": "",
	          "Hole(Physical)": "",
	          "Character Line Segment": "",
	          "Boundary Line": "",
	          "Physical Degradation": "",
	          "Page Boundary": "",
	          "Character Component": "",
	          "Picture": "",
	          "Decorator": "",
	          "Library Marker": ""
	        },
	        "default_options": {}
	      },
	      "Comments": {
	        "type": "text",
	        "description": "",
	        "default_value": ""
	      }
	    },
	    "file": {}
	  },
	  "file": \""""+str(name)+"""\"
	}
	"""

	rgns=""
	# print(scale,"scale")
	# print(scale1,"scale1")
	arr1 = np.zeros(11)
	count1 = np.zeros(11)
	avg1 = np.zeros(11)
	# print("intial")
	# print(arr1,"arr")
	# print(count1,"count")
	ROOT_DIR = os.path.abspath("./Instance-segmentation-master")
	perimeter_path = ROOT_DIR+"/main/doc/"
	loaded_avg = np.load(perimeter_path+'perimeter.npy')
	# arr = arr
	# count = count
	for i in range(len(cls)):
		if i!=(-1):
			
			try:
				k = np.array(contours[i][0])
			except:
				#error_out = """{
				#"error": ["1"]				
				#}"""
				#error_out = {}
				#error_out['error'] = 1
				return []

			# d = k[0][0]
			# print(type(d),"d")
			# print(scale,"scale")
			# k=(k *(1/scale))
			k=k.astype(int)
			arr1=np.array(arr1)
			# count=count
			
			# print(k[0][0])
			# k[:,0] = np.rint(k[:,0] * (1/ scale))
			# k[:,1] = np.rint(k[:,1] * (1/ scale1))
			# d = k[0][0]
			# print(type(d),"d")
			k= np.array(k)
			# print(k.shape,"kshape")
			# print(k," ith k",i)
			ln=len(contours[i][0])
			mid = int(ln/2)
			# k1=k[0:mid,:]
			# k2=k[mid:ln-1,:]
			k1=k[0:ln-1,:]
			# print(k1,"ith k1",i)
			# print(k1.shape,"k1shape")
			# print(k2,"ith k2",i)
			# print(k2.shape,"k2shape")
			# from rdp import rdp
			# from simplification.cutil import simplify_coords, simplify_coordsvw
			# from polysimplify import VWSimplifier
			import visvalingamwyatt as vw
			# simplifier = vw.Simplifier(points)

# Simplify by percentage of points to keep
      # simplifier.simplify(ratio=0.5)
			simplifier1 = vw.Simplifier(k1)
			# simplifier.simplify(ratio=0.5)
			n1=int(0.020*k1.shape[0])
			
			# if(n1<4):
			# 	n1=4

			# perimeter
			perimeter = Polygon(k1).length
			# print(perimeter,"pppppppppppp")

			sub_loaded =  np.absolute(loaded_avg - perimeter)

			index_min = np.argmin(sub_loaded)
			# print(sub_loaded ,"subloaded")
			# print(index_min,"index_min")
			# if it is BG
			if(index_min)==0:
				n1=int(0.020*k1.shape[0])
			#if it is H-V
			if(index_min)==1:
				n1=int(0.040*k1.shape[0])

			#if it is H
			if(index_min)==2:
				n1=int(0.040*k1.shape[0])
			# cls
			if(index_min)==3:
				n1=int(0.020*k1.shape[0])
			# pd
			if(index_min)==4:
				n1=int(0.030*k1.shape[0])
			# pb
			if(index_min)==5:
				n1=int(0.010*k1.shape[0])
			# cc
			if(index_min)==6:
				n1=int(0.040*k1.shape[0])
			# p
			if(index_min)==7:
				n1=int(0.040*k1.shape[0])
			# d
			if(index_min)==8:
				n1=int(0.040*k1.shape[0])
			# lm
			if(index_min)==9:
				n1=int(0.040*k1.shape[0])
			# bl
			if(index_min)==10:
				n1=int(0.020*k1.shape[0])

			if n1<4:
				n1=4
			


			
			# print(n1,"n1")
			# n2=int(0.025*k2.shape[0])
			# print(n2,"n2")


			
			rdpk1=np.array(simplifier1.simplify(number=n1))
			# simplifier2 = vw.Simplifier(k2)
			# simplifier.simplify(ratio=0.5)
			# rdpk2=np.array(simplifier2.simplify(number=n2))
			# rdpk1= rdp(k1,epsilon=1)
			# rdpk2= rdp(k2,epsilon=1)
			# print(rdpk1,"ith rdpk1",i)
			# print(rdpk1.shape,"rdpk1shape")
			# print(rdpk2,"ith rdpk2",i)
			# print(rdpk2.shape,"rdpk2shape")
			# final= np.concatenate((rdpk1, rdpk2), axis=0)
			final=rdpk1
			# print(final.shape[0],"finalshape")
			# print(final[0][0],"final")
			i = int(i)
			finallist = np.array(final).tolist()
			# perimeter
			# perimeter = Polygon(final).length
			# 
			# sub_loaded =  abs.absolute(loaded_avg - perimeter)

			# print(perimeter,"perimeter of i - ", i)
			# print(cls[i])
			arr1[cls[i]] += perimeter
			count1[cls[i]] += 1
			avg1[cls[i]] = (arr1[cls[i]]/count1[cls[i]])
			# print(arr1,"arr after i - ",i)
			# print(count1,"count after i - ",i)
			# print(avg1,"avg after i",i)

			# storingarray(arr,count)
			length=final.shape[0]
			str1=""
			str2=""
			for j in range(length):

				str1+=str(int((final[j][0]-padding[0][0])*(1/scale)))
				
				str1+=","
				str1+='\n'
			for j in range(length):

				str2+=str(int((final[j][1]-padding[1][0])*(1/scale)))
				# g=0
				str2+=","
				str2+='\n'
			str1=str1[:-2]
			str2=str2[:-2]
			rg="""{
	          "shape_attributes": {
	            "name": "polygon",
	            "all_points_x": [ """+ str2+"""],
	            "all_points_y": ["""+str1+ """]
	          },
	          "region_attributes": {
	            "Spatial Annotation":\""""+str(classes[cls[i]])+"""\",
	            "Comments": ""
	          },
	          "timestamp": {
	            "StartingTime": 6016533,
	            "EndTime": 6035060
	          }
	        }"""
			
			if(i!=len(cls)-1):
				rg+=","
			rgns+=rg

	    # if(i!=len(cls)-1):

	    #   rg+=","
	    # rgns+=rg
	print("done")

	# for updating the perimeter values
	# print(np.load('perimeter.npy'),"old")
	# loaded_avg = np.load('perimeter.npy')
	new_avg= np.zeros(11)
	for i in range(11):
		if((int(count1[i])!=0) and (int(loaded_avg[i])!=0)):
			

			new_avg[i]= (loaded_avg[i] + avg1[i])
			new_avg[i] = new_avg[i] / 2
			
		else:
			
			new_avg[i] = loaded_avg[i] + avg1[i]

	
	np.save(perimeter_path+'perimeter.npy', new_avg)
	# print(np.load('perimeter.npy'),"new")
	#end of updating the perimeter values
				
  
				
				


	# k=np.array(contours)
	# print(k,"k")
	# print(k.shape[0],"shape1")


	# for i in range(len(cls)):

	#     str1=""
	#     str2=""
	#     ln=len(contours[i][0])
			
	#     print(ln,"lrn")
	#     for j in range(ln):

	#         if(j%20==0):
	#             str1+=str(contours[i][0][j][0]-padding[0][0])
	#             str1+=','
	#             str1+='\n'
	#     for j in range(ln):
	#         if(j%20==0):
	#             str2+=str(contours[i][0][j][1]-padding[1][0])
	#             str2+=','
	#             str2+='\n'
	#     str1=str1[:-2]
	#     str2=str2[:-2]
	    # rg="""{
	    #       "shape_attributes": {
	    #         "name": "polygon",
	    #         "all_points_x": [ """+ str2+"""],
	    #         "all_points_y": ["""+str1+ """]
	    #       },
	    #       "region_attributes": {
	    #         "Spatial Annotation":\""""+str(classes[cls[i]])+"""\",
	    #         "Comments": ""
	    #       },
	    #       "timestamp": {
	    #         "StartingTime": 6016533,
	    #         "EndTime": 6035060
	    #       }
	    #     }"""
	    # if(i!=len(cls)-1):
	    #     rg+=","
	    # rgns+=rg

	with open (perimeter_path+'save.json','w') as f:
	    f.write(strt)
	    f.write(rgns)
	    f.write(end)
	h, w = image.shape[:2]
	image=image[padding[0][0]:h-padding[0][1],padding[1][0]:w-padding[1][1]]
	plt.savefig(OUTPUTPATH,bbox_inches='tight')
	# print(arr)
	# print(count)


	#final_output = strt + rgns + end
	final_output = '{"output": [' + rgns + '], "file": "' + str(name) + '", "url": "' + str(filename) + '"}'
	#print(final_output)
	return final_output







HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 30000       # Port to listen on (non-privileged ports are > 1023)


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
			output_json = modeltest1(input_json['fileurl'], [1,2,3], input_json['filename'])
			data.inb += json.dumps(output_json)
			#data.inb += output_json
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
