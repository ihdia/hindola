import socket
import selectors
import types
import json
import threading

class Queue:
	def __init__(self):
		self.items = []
 
	def is_empty(self):
		return self.items == []
 
	def enqueue(self, data):
		self.items.append(data)
 
	def dequeue(self):
		return self.items.pop(0)
 
q_auto = Queue()
q_semi_auto = Queue()

sel = selectors.DefaultSelector()
sel1 = selectors.DefaultSelector()
sel2 = selectors.DefaultSelector()


def service_automatic(autokey, automask):
	global auto_register_count
	autosock = autokey.fileobj
	autodata = autokey.data
	if automask & selectors.EVENT_READ:
		autorecv_data = autosock.recv(500024)  # Should be ready to read
		if autorecv_data:
			print('received', repr(autorecv_data.decode('utf-8')), 'from connection')
			autodata.recv_total += len(autorecv_data.decode('utf-8'))
			print('closing connection to ML engine')
			sel1.unregister(autosock)
			auto_register_count -= 1
			autosock.close()
			sent = autodata.old_sock.sendall(autorecv_data)
			autorecv_data = ''
			print('closing connection to', autodata.old_sock_addr)
			sel.unregister(autodata.old_sock)
			autodata.old_sock.close()
		#if not autorecv_data or autodata.recv_total == autodata.msg_total:
		#if not autorecv_data:
		#	print('closing connection to ML engine')
		#	sel1.unregister(autosock)
		#	auto_register_count -= 1
		#	autosock.close()
		#	if autorecv_data:
		#		sent = autodata.old_sock.sendall(autorecv_data)
		#		autorecv_data = ''
		#	print('closing connection to', autodata.old_sock_addr)
		#	sel.unregister(autodata.old_sock)
		#	autodata.old_sock.close()
			
	if automask & selectors.EVENT_WRITE:
		#if not data.outb and data.messages:
			#data.outb = data.messages.pop(0)
		#if data.outb:
		if autodata.messages:
			print('sending', repr(autodata.messages), 'to connection')
			autosent = autosock.sendall((autodata.messages).encode('utf-8'))  # Should be ready to write
			autodata.messages = ''
			#data.outb = data.outb[sent:]

def service_request_automatic(host, port):
	global auto_register_count
	while True:
		if q_auto.is_empty() == False:
			mask = (q_auto.items[0])['mask']
			if mask & selectors.EVENT_WRITE:
				
				sock = (q_auto.items[0])['client']
				sock_addr = (q_auto.items[0])['client_addr']


				server_addr = (host, port)
				autosock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				autosock.setblocking(False)
				autosock.connect_ex(server_addr)
				e = selectors.EVENT_READ | selectors.EVENT_WRITE
				autodata = types.SimpleNamespace(
									 #msg_total=sum(len(m) for m in messages),
									 msg_total=len((q_auto.items[0])['args']),
									 recv_total=0,
									 messages=(q_auto.items[0])['args'],
									 old_sock=sock,
									 old_sock_addr=sock_addr,
									 #outb=b'')
									 )
				sel1.register(autosock, e, data=autodata)
				auto_register_count += 1
				


				#print(json.loads((q.items[0])['args']))
				#print(q.items[0])
				#sent = sock.sendall((q.items[0])['args'].encode('utf-8'))  # Should be ready to write
				q_auto.dequeue()
		if(auto_register_count != 0):
			e = sel1.select()
			for autokey, automask in e:
				service_automatic(autokey, automask)


def service_semi_automatic(semi_autokey, semi_automask):
	global semi_register_count
	semi_autosock = semi_autokey.fileobj
	semi_autodata = semi_autokey.data
	if semi_automask & selectors.EVENT_READ:
		semi_autorecv_data = semi_autosock.recv(500024)  # Should be ready to read
		if semi_autorecv_data:
			print('received', repr(semi_autorecv_data.decode('utf-8')), 'from connection')
			semi_autodata.recv_total += len(semi_autorecv_data.decode('utf-8'))
			print('closing connection to ML engine')
			sel2.unregister(semi_autosock)
			semi_register_count -= 1
			semi_autosock.close()
			sent = semi_autodata.old_sock.sendall(semi_autorecv_data)
			semi_autorecv_data = ''
			print('closing connection to', semi_autodata.old_sock_addr)
			sel.unregister(semi_autodata.old_sock)
			semi_autodata.old_sock.close()
		#if not autorecv_data or autodata.recv_total == autodata.msg_total:
		#if not autorecv_data:
		#	print('closing connection to ML engine')
		#	sel2.unregister(autosock)
		#	semi_register_count -= 1
		#	autosock.close()
		#	if autorecv_data:
		#		sent = autodata.old_sock.sendall(autorecv_data)
		#		autorecv_data = ''
		#	print('closing connection to', autodata.old_sock_addr)
		#	sel.unregister(autodata.old_sock)
		#	autodata.old_sock.close()
			
	if semi_automask & selectors.EVENT_WRITE:
		#if not data.outb and data.messages:
			#data.outb = data.messages.pop(0)
		#if data.outb:
		if semi_autodata.messages:
			print('sending', repr(semi_autodata.messages), 'to connection')
			semi_autosent = semi_autosock.sendall((semi_autodata.messages).encode('utf-8'))  # Should be ready to write
			semi_autodata.messages = ''
			#data.outb = data.outb[sent:]

def service_request_semi_automatic(host, port):
	global semi_register_count
	while True:
		if q_semi_auto.is_empty() == False:
			mask = (q_semi_auto.items[0])['mask']
			if mask & selectors.EVENT_WRITE:
				
				sock = (q_semi_auto.items[0])['client']
				sock_addr = (q_semi_auto.items[0])['client_addr']


				server_addr = (host, port)
				semi_autosock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				semi_autosock.setblocking(False)
				semi_autosock.connect_ex(server_addr)
				e = selectors.EVENT_READ | selectors.EVENT_WRITE
				semi_autodata = types.SimpleNamespace(
									 #msg_total=sum(len(m) for m in messages),
									 msg_total=len((q_semi_auto.items[0])['args']),
									 recv_total=0,
									 messages=(q_semi_auto.items[0])['args'],
									 old_sock=sock,
									 old_sock_addr=sock_addr,
									 #outb=b'')
									 )
				sel2.register(semi_autosock, e, data=semi_autodata)
				semi_register_count += 1
				


				#print(json.loads((q.items[0])['args']))
				#print(q.items[0])
				#sent = sock.sendall((q.items[0])['args'].encode('utf-8'))  # Should be ready to write
				q_semi_auto.dequeue()
		if(semi_register_count != 0):
			e = sel2.select()
			for semi_autokey, semi_automask in e:
				service_semi_automatic(semi_autokey, semi_automask)

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
			queue_entry = {'args': data.outb, 'client': sock, 'client_addr': data.addr, 'mask': mask}
			#flag_checking_json = json.loads(data.outb)
			flag_checking_json = eval(data.outb)
			if (flag_checking_json['flag'] == 1):
				q_auto.enqueue(queue_entry)
			elif (flag_checking_json['flag'] == 2):
				q_semi_auto.enqueue(queue_entry)
			data.outb = ''
		else:
			#print('closing connection to', data.addr)
			#sel.unregister(sock)
			#sock.close()
			pass
	if mask & selectors.EVENT_WRITE:
		pass
	#	if data.outb:
	#		queue_entry = {'args': data.outb, 'client': sock, 'mask': mask}
	#		q.enqueue(queue_entry)
	#		if q.is_empty() == False:
	#			print(json.loads((q.items[0])['args']))
	#			#print(q.items[0])
	#			q.dequeue()
	#		sent = sock.sendall((q.items[0])['args'].encode('utf-8'))  # Should be ready to write
	#		data.outb = ''

#@socketio.on('autoenqueue')
#def autoenqueue():
#	q.enqueue(1)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 54321        # Port to listen on (non-privileged ports are > 1023)

semiAutomaticHOST = '127.0.0.1'
semiAutomaticPORT = 40000

AutomaticHOST = '127.0.0.1'
AutomaticPORT = 30000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	s.setblocking(False)
	sel.register(s, selectors.EVENT_READ, data=None)
	
	auto_register_count = 0
	semi_register_count = 0

	auto_request_process = threading.Thread(target=service_request_automatic, args=(AutomaticHOST, AutomaticPORT), daemon=True)
	auto_request_process.start()
	semi_request_process = threading.Thread(target=service_request_semi_automatic, args=(semiAutomaticHOST, semiAutomaticPORT), daemon=True)
	semi_request_process.start()

	while True:
		events = sel.select()
		#print(q.items)
		for key, mask in events:
			if key.data is None:
				accept_wrapper(key.fileobj)
			else:
				service_connection(key, mask)