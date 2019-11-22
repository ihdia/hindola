from myproject import app,db,socketio
from flask import render_template, redirect, request, url_for, flash,abort,jsonify,session
from flask_login import login_user,login_required,logout_user,current_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
import time
from flask_socketio import  send,emit
import sys
# from flask_pymongo import PyMongo,MongoClient
from flask import Response
# from bson.json_util import loads
import json
import os, os.path
####################################################
# Intelligent Mode Socket configurations
import socket
import selectors
import types

sel = selectors.DefaultSelector()
flag = 0;
autoflag = 0;
####################################################
# MySQL configurations
import pymysql
from flaskext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = sys.argv[1]
app.config['MYSQL_DATABASE_PASSWORD'] = sys.argv[2]
app.config['MYSQL_DATABASE_DB'] = sys.argv[3]
app.config['MYSQL_DATABASE_HOST'] = sys.argv[4]
mysql.init_app(app)
####################################################
#arg6 = sys.argv[6]
arg6 = 'main/myproject/static/imgdata'

stat_B = 0
stat_D = 0

@socketio.on('myconnection')
def test_connect(msg):
	# TODO: push all in_process uid to uid table
	print(msg)

# r = json.dumps(jsonfile)
# print(type(r)) #Output str
# loaded_r = json.loads(r)
# print(type(loaded_r)) #Output dict
# t=json.load(json.dumps(jsonfile))


def service_connection(key, mask):
		global flag
		sock = key.fileobj
		data = key.data
		if mask & selectors.EVENT_READ:
			recv_data = sock.recv(500024)  # Should be ready to read
			if recv_data:
				print('received', recv_data, 'from connection', data.connid)
				json_output_data = json.loads(recv_data)
				#json_output_data = eval(recv_data)
				if (json_output_data['flag'] == 1):
					emit('autoResponse', recv_data.decode('utf-8'))
					filename=str(json_output_data['file'])
					tempu = str(json_output_data['url'])
					print(tempu)
					print('filename saved: '+ filename)
					conn = mysql.connect()
					cursor = conn.cursor(pymysql.cursors.DictCursor)
					#newfullpath=pathtojsonv1+filename+'.json'
					#print(newfullpath)
					#file=open(newfullpath,'w+')
					json_output_data = json.dumps(json_output_data)
					sql = 'SELECT * FROM json_v1 WHERE filename=%s;'
					d = (filename)
					cursor.execute(sql, d)
					record = cursor.fetchone()
					conn.commit()

					if (not record):
						sql = 'INSERT INTO json_v1 (filename, json_data, fileurl) VALUES (%s, %s, %s);'
						d = (filename, json_output_data, tempu)
						cursor.execute(sql, d)
						conn.commit()
					else:
						sql = 'DELETE FROM json_v1 WHERE filename=%s;'
						d = (filename)
						cursor.execute(sql, d)
						conn.commit()
						sql = 'INSERT INTO json_v1 (filename, json_data, fileurl) VALUES (%s, %s, %s);'
						d = (filename, json_output_data, tempu)
						cursor.execute(sql, d)
						conn.commit()
					#file.write(json_output_data)
					#file.close()

				elif (json_output_data['flag'] == 2):
					emit('semi_autoResponse', recv_data.decode('utf-8'))
					conn = mysql.connect()
					cursor = conn.cursor()
					cursor.execute("SELECT * from imagelinks LIMIT 1;")
					rows = cursor.fetchone()
					conn.commit()

					if rows:
						conn = mysql.connect()
						cursor = conn.cursor(pymysql.cursors.DictCursor)
		
						sql = 'SELECT * FROM imagelinks WHERE links=%s;'
						d = (json_output_data['url'])
						cursor.execute(sql, d)
						imgLinks = cursor.fetchone()
						conn.commit()
						# print(imgLinks)
						#filename=pathtojsonv1 + 'bb-' + str(imgLinks['file']) + '.json'
						filename='bb-' + str(imgLinks['file'])
						sql = 'SELECT * FROM json_v1 WHERE filename=%s;'
						d = (filename)
						cursor.execute(sql, d)
						record = cursor.fetchone()
						conn.commit()
						#if (not os.path.isfile(filename)):
						if (not record):
							print('filename saved: '+ filename)
							#file=open(filename,'w+')
							output = {}
							output['regions'] = []
							output['regions'].append(json_output_data)
							output = json.dumps(output)
							sql = 'INSERT INTO json_v1 (filename, json_data, fileurl) VALUES (%s, %s, %s);'
							d = (filename, output, imgLinks['links'])
							cursor.execute(sql, d)
							conn.commit()
							#file.write(output)
							#file.close()
						else:
							#file=open(filename,'r')
							jsondata = json.loads(record['json_data'])
							#data = json.load(file)
							jsondata['regions'].append(json_output_data)
							jsondata = json.dumps(jsondata)
							sql = 'DELETE from json_v1 WHERE filename=%s;'
							d = (filename)
							cursor.execute(sql, d)
							conn.commit()
							sql = 'INSERT INTO json_v1 (filename, json_data, fileurl) VALUES (%s, %s, %s);'
							d = (filename, jsondata, imgLinks['links'])
							cursor.execute(sql, d)
							conn.commit()
							#file.close()
							#file=open(filename,'')
							#file.write(data)
							#file.close()
					else:
						print("There are no links in the database!\n")

				#time.sleep(10)
				data.recv_total += len(recv_data.decode('utf-8'))
			if not recv_data or data.recv_total == data.msg_total:
				print('closing connection', data.connid)
				sel.unregister(sock)
				flag -= 1
				sock.close()
		if mask & selectors.EVENT_WRITE:
			#if not data.outb and data.messages:
				#data.outb = data.messages.pop(0)
			#if data.outb:
			if data.messages:
				print('sending', repr(data.messages), 'to connection', data.connid)
				sent = sock.sendall((data.messages).encode('utf-8'))  # Should be ready to write
				data.messages = ''
				#data.outb = data.outb[sent:]

def start_connections(host, port, num_conns, messages):
		global flag
		server_addr = (host, port)
		for i in range(0, num_conns):
			connid = i + 1
			print('starting connection', connid, 'to', server_addr)
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setblocking(False)
			sock.connect_ex(server_addr)
			events = selectors.EVENT_READ | selectors.EVENT_WRITE
			data = types.SimpleNamespace(connid=connid,
									 #msg_total=sum(len(m) for m in messages),
									 msg_total=len(json.dumps(messages[connid-1])),
									 recv_total=0,
									 messages=json.dumps(messages[connid-1]),
									 #outb=b'')
									 )
			sel.register(sock, events, data=data)
			flag += 1
	
		while flag != 0:
			events = sel.select()
			for key, mask in events:
				service_connection(key, mask)

@socketio.on('send_intelligent_details')
def send_intelligent_details(data):

	HOST = '127.0.0.1'  # The server's hostname or IP address
	PORT = 54321       # The port used by the server

	messages = [data]
	num_conns = 1

	start_connections(HOST, PORT, num_conns, messages)
	#socketio.start_background_task(target=lambda: start_connections(HOST, PORT, num_conns, messages))

@socketio.on('select_collection')
def select_collection():

	# select_from_collection('name')
	n=0
	# uids=UIDS.query.all()

	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute('SET NAMES utf8mb4') 
	cursor.execute("SET CHARACTER SET utf8mb4") 
	cursor.execute("SET character_set_connection=utf8mb4")
	cursor.execute("SELECT * from imagelinks LIMIT 1;")
	rows = cursor.fetchone()
	conn.commit()

	# print("Allocated "+str(len(uids)))
	# print(random.randint(1,len(uids)))
	if rows:
		# n=randint(1,len(uids))
		# db.session.delete(uids[n])
		# db.session.commit()

		# SELECT * FROM uids ORDER BY RAND() LIMIT 1
		conn = mysql.connect()
		# cursor = conn.cursor()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		global stat_B
		cursor.execute("SELECT * FROM imagelinks;")
		imgLinks = cursor.fetchall()
		conn.commit()
		urls = []
		for link in imgLinks:
			urls.append(link['links'])
		temp_urls = set()
		for url in urls:
			if(arg6[-1] == '/'):
				linkprefix = arg6
			else:
				linkprefix = arg6 + '/'			
			prefixlen = len(linkprefix)
			if(url[0:prefixlen] == linkprefix):
				rest_of_url = url[prefixlen:]
				temp_urls.add(rest_of_url.split('/')[0].strip())
		urls = set()
		for url in temp_urls:
			urls.add(url.replace('%20', ' '))
		# print(urls)
		urls = list(urls)
		urls = sorted(urls)
		stat_B = 0

		jsonfile={}
		# give file id ,not n
		jsonfile['urls']=urls
		data=json.dumps(jsonfile)

		emit('fetchCollResponse', str(data))
	else:
		# TODO: handle this exception
		emit('fetchCollResponse', str("none"))

@socketio.on('select_from_collection')
def select_from_collection(collection):

	# select_from_collection('name')
	n=0
	# uids=UIDS.query.all()

	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute('SET NAMES utf8mb4') 
	cursor.execute("SET CHARACTER SET utf8mb4") 
	cursor.execute("SET character_set_connection=utf8mb4")
	cursor.execute("SELECT * from imagelinks LIMIT 1;")
	rows = cursor.fetchone()
	conn.commit()

	# print("Allocated "+str(len(uids)))
	# print(random.randint(1,len(uids)))
	if rows:
		# n=randint(1,len(uids))
		# db.session.delete(uids[n])
		# db.session.commit()

		# SELECT * FROM uids ORDER BY RAND() LIMIT 1
		conn = mysql.connect()
		# cursor = conn.cursor()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		global stat_B
		cursor.execute("SELECT * FROM imagelinks;")
		imgLinks = cursor.fetchall()
		conn.commit()
		urls = []
		for link in imgLinks:
			urls.append(link['links'])
		temp_urls = set()
		for url in urls:
			if(arg6[-1] == '/'):
				linkprefix = arg6 + collection + '/'
			else:
				linkprefix = arg6 + '/' + collection + '/'
			prefixlen = len(linkprefix)
			if(url[0:prefixlen] == linkprefix):
				rest_of_url = url[prefixlen:]
				temp_urls.add(rest_of_url.split('/')[0].strip())
		urls = set()
		for url in temp_urls:
			urls.add(url.replace('%20', ' '))
		# print(urls)
		urls = list(urls)
		urls = sorted(urls)
		stat_B = 0

		jsonfile={}
		# give file id ,not n
		jsonfile['urls']=urls
		data=json.dumps(jsonfile)

		emit('fetchBookResponse', str(data))
	else:
		# TODO: handle this exception
		emit('fetchBookResponse', str("none"))

@socketio.on('select_from_book')
def select_from_book(data):

	# select_from_book('name')
	n=0
	# uids=UIDS.query.all()
	data['book'] = data['book'].replace(' ', '%20')

	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute('SET NAMES utf8mb4')
	cursor.execute("SET CHARACTER SET utf8mb4")
	cursor.execute("SET character_set_connection=utf8mb4")
	cursor.execute("SELECT * from imagelinks LIMIT 1;")
	rows = cursor.fetchone()
	conn.commit()

	# print("Allocated "+str(len(uids)))
	# print(random.randint(1,len(uids)))
	if rows:
		# n=randint(1,len(uids))
		# db.session.delete(uids[n])
		# db.session.commit()

		# SELECT * FROM uids ORDER BY RAND() LIMIT 1
		conn = mysql.connect()
		# cursor = conn.cursor()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		global stat_B
		
		sql = 'SELECT * FROM imagelinks WHERE links LIKE \"%' + data['book'] + '%\";'
		cursor.execute(sql)
		imgLinks = cursor.fetchall()
		conn.commit()
		urls = []
		# print(imgLinks)
		for link in imgLinks:
			tdic={}
			# give file id ,not n
			tdic['file']=link['file']
			tdic['links']=str(link['links'])
			urls.append(tdic)      
		print(urls)
		urls = sorted(urls, key = lambda i: i['links'])
		print(urls)
		stat_B = 0

		jsonfile={}
		# give file id ,not n
		jsonfile['urls']=urls
		data=json.dumps(jsonfile)
		#print(data)

		emit('fetchPageResponse', str(data))
	else:
		# TODO: handle this exception
		emit('fetchPageResponse', str("none"))

@socketio.on('checkPageRequests')
def checkPageRequests(data):
	
	sql = "SELECT * from pagerequests WHERE name=%s LIMIT 1"
	d = (data)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, d)
	request = cursor.fetchone()
	print(request)
	conn.commit()
	
	if request:
		jsonfile = {}
		jsonfile['check'] = "true"
		jsonfile['name'] = request[0]
		jsonfile['book'] = request[1]
		jsonfile['start_page'] = request[2]
		jsonfile['current_page'] = request[3]
		jsonfile['end_page'] = request[4]
		data = json.dumps(jsonfile)
		print('ayy lmao')

		emit('obtainPageRequests', str(data))
	else:
		jsonfile = {}
		jsonfile['check'] = "false"
		data = json.dumps(jsonfile)

		emit('obtainPageRequests', str(data))

@socketio.on('insert_page_request')
def insert_page_request(data):
	
	sql = "INSERT INTO pagerequests (name, book, start_page, current_page, end_page, skipped) VALUES(%s, %s, %s, %s, %s, %s)"
	d = (data['anno_name'], data['bookname'], data['startpage'], data['startpage'], data['endpage'], 0)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, d)
	conn.commit()
	#print('request inserted by ' + data['anno_name'] + ' for book ' + data['bookname'] + ' for page ' + data['startpage'] + ' to ' + data['endpage'])


@socketio.on('update_page_request')
def update_page_request(data):
	
	if (data['skipt'] == 1):
		sql = "UPDATE pagerequests SET current_page=%s, skipped=skipped+1 WHERE name=%s"
		d = (data['startpage'], data['anno_name'])
	else:
		sql = "UPDATE pagerequests SET current_page=%s WHERE name=%s"
		d = (data['startpage'], data['anno_name'])
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, d)
	conn.commit()
	#print('request updated to ' + data['startpage'] + ' for ' + data['anno_name'])

@socketio.on('delete_page_request')
def delete_page_request(data):
	
	sql = "DELETE FROM pagerequests WHERE name=%s"
	d = (data)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, d)
	conn.commit()
	#print('request by ' + data['anno_name'] + ' deleted')
	
@socketio.on('update_book_completion')
def update_book_completion(data):
	
	if (data['mode'] == 0):
		sql = "UPDATE bookcompletion SET completed_pages = completed_pages + 1  WHERE name=%s"
		d = (data['bookname'])
	elif (data['mode'] == 1):
		sql = 'INSERT INTO bookcompletion (name, total_pages, completed_pages) VALUES(%s, %s, 0) ON DUPLICATE KEY UPDATE total_pages=%s'
		d = (data['bookname'], data['length'], data['length'])
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, d)
	conn.commit()


@socketio.on('fetchUID')
def fetchUID(aid):
	#  added to request queue
	# caid=RequestUIDS(ruid=aid)
	# db.session.add(caid)
	# db.session.commit()
	print('AID: ',aid, 'Requesting: ')

	sql = "INSERT INTO ruids (ruid) VALUES(%s)"
	data = (aid)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, data)
	conn.commit()


	time.sleep(1)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("DELETE FROM ruids limit 1;")
	conn.commit()

	conn = mysql.connect()
	# cursor = conn.cursor()
	cursor = conn.cursor(pymysql.cursors.DictCursor)

	sql2 = "SELECT COUNT(*) FROM corrections;"
	cursor.execute(sql2)
	de = cursor.fetchone()
	de = de['COUNT(*)']
	print(de)
	global stat_D
	global stat_filepath
	if de <= 0:
		cursor.execute("SELECT * FROM puids ORDER BY RAND() LIMIT 1;")
		pfile = cursor.fetchone()
		conn.commit()
		stat_D = 0
	else:
		cursor.execute("SELECT * FROM corrections ORDER BY RAND() LIMIT 1;")
		pfile = cursor.fetchone()
		conn.commit()
		filename=pfile['pfile']
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM corrections WHERE pfile=%s",filename)
		stat_D = 1
		stat_filepath = pfile['pfilepath']
		conn.commit()
	
	


	# GET THE FIRST FILE IN modified folder
	# TODO: FIND THE FILE Number
	if pfile:
		# TODO(1): choose randomly from puids table
		filename=pfile['pfile']
		filepath=pfile['pfilepath']
		##############################################
		# data='bhoomi_ANINGYA%20VYAKHYA_PIVS_001_16_Sun Jan 13 16:00:33 2019.json'
		print(filepath)
		file=open(filepath,'r')
		data=str(file.read())
		file.close()
		############### uncomment below #########
		# TODO: add a session variable here with a key as "uid_by_aid" and value ="uid-aid"
		# if not session['uid_by_aid']:
			# session['uid_by_aid'] = str(uids[0].uid) +'_'+ str(current_user.id)
		#############################################

		#  add the info into table
		#  get the image links also

		# imagelink=ImageLinksi.query.filter_by(file=filename).first()
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
	
	
		sql="SELECT * FROM imagelinks WHERE file=%s LIMIT 1;"
		d=(filename)
		cursor.execute(sql,d)
		imagelinks=cursor.fetchone()
		conn.commit()

		dateOfAnnotation=time.ctime()
		status="in_process"
		# Info database, mark status Column as "in_process"

			# info=Info(str(current_user.username),filename,status,dateOfAnnotation,str(imagelink.links))
			# info=Info(file=filename,username=current_user.username,status=status,dateOfAnnotation,str(imagelink.links))
			# db.session.add(info)
			# db.sess ion.commit()

		sql = "INSERT INTO info(username, file,status,date,localurl) VALUES(%s, %s, %s,%s,%s)"
		d = (current_user.username,filename,status,dateOfAnnotation,imagelinks['links'])
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql,d)
		conn.commit()

		emit('fetchUIDAnswer',str(data))
		# emit('fetchUIDAnswer',"no json in folder")
	else:
		emit('fetchUIDAnswer',"na")



@socketio.on('mydata')
def mydata(data):

	# TODO(2): check whether the data is in puids if there update the path accordingly....
	print(type(data)) # <class 'str'>
	# print('received data: ' + (data))
	jsonfile=json.loads(data)
	# print(jsonfile)
	filename=str(jsonfile['file'])

	print('filename saved: '+ filename)
	###################################
	# delete in the modified path
	# fullpath=pathtomodifiedjson+filename+'_'+str(curr_time)'.json'
	# fullpath=pathtomodifiedjson+filename+'.json'
	# print(fullpath)
	# try:
	#     os.remove(fullpath)
	# except OSError:
	#     print("file not exist in modified directory")
	###################################

	#curr_time=time.ctime()
	#newfullpath=pathtojson+filename+'_'+curr_time+'.json'
	
	#newfullpath=pathtojsonv2+filename+'.json'
	primekey = list(jsonfile['_via_img_metadata'])[0]
	tempu = str(((jsonfile['_via_img_metadata'])[primekey])['filename'])
	print(tempu)
	sql = 'SELECT * FROM json_v2 WHERE filename=%s;'
	d = (filename)
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	cursor.execute(sql, d)
	record = cursor.fetchone()
	conn.commit()

	if (not record):
		sql = 'INSERT INTO json_v2 (filename, json_data, fileurl) VALUES (%s, %s, %s);'
		d = (filename, data, tempu)
		cursor.execute(sql, d)
		conn.commit()

	else:
		sql = 'DELETE FROM json_v2 WHERE filename=%s;'
		d = (filename)
		cursor.execute(sql, d)
		conn.commit()
		sql = 'INSERT INTO json_v2 (filename, json_data, fileurl) VALUES (%s, %s, %s);'
		d = (filename, json_output_data, tempu)
		cursor.execute(sql, d)
		conn.commit()

	#print(newfullpath)
	#file=open(newfullpath,'w+')
	#file.write(data)
	#file.close()

	#TODO: check if filename as pfile exist in puid table, update the table column  "pfilepath"
	sql = "SELECT * from puids where pfile = %s LIMIT 1"
	d = filename
	#conn = mysql.connect()
	#cursor = conn.cursor(pymysql.cursors.DictCursor)
	cursor.execute(sql,d)
	puidtemp=cursor.fetchone()
	conn.commit()


	# put the file in processed .
	# pfile=PUIDS(pfile=filename,pfilepath=fullpath)
	# db.session.add(pfile)
	# db.session.commit()
	save_date = time.ctime()
	if puidtemp:
		# saving annotated image
		# update the puid table
		print("saving existing annotated image.....")
		sql = "UPDATE puids SET pfilepath=%s, saved_date=%s WHERE pfile=%s"
		d = (filename, save_date, filename)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, d)
	else:
		# saving new Image
		print("saving new annotated image.....")
		sql = "INSERT INTO puids(pfile, pfilepath, saved_date) VALUES(%s, %s,%s)"
		data = (filename, filename, save_date)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
	
	conn.commit()


	in_process="in_process"
	status="annotated"
	# temp = Info.query.filter_by(file=filename,username=str(current_user.username)).first()
	# temp.status=status
	# temp.dateOfAnnotation=str(temp.dateOfAnnotation)+"---"+str(time.ctime());
	# db.session.commit()

	sql = "UPDATE info SET status=%s WHERE file=%s and username=%s"
	d = (status,filename,current_user.username)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, d)
	conn.commit()

	print("saved annotated file: "+filename+" by User  :"+ str(current_user.username) )
	emit('saveconfirmation',"saved")

@socketio.on('request_cancelled')
def request_cancelled(n):
	filename=str(n)
	# putting back to UIDS
	# uid=UIDS(ufile=filename)
	# db.session.add(uid)
	# db.session.commit()
	print("request cancelled")

	conn = mysql.connect()
	cursor = conn.cursor()
	sql="insert into uids(ufile) values(%s)"
	data=(filename)
	cursor.execute(sql,data)
	conn.commit()

	# temp = Info.query.filter_by(file=filename,username=str(current_user.username)).first()
	# if temp:
	#     db.session.delete(temp)
	#     db.session.commit()

	conn = mysql.connect()
	cursor = conn.cursor()
	sql="DELETE from info WHERE file=%s and username=%s"
	data=(filename,current_user.username)
	cursor.execute(sql,data)
	conn.commit()


@socketio.on('fetchNext')
def fetchNext(n):
	filename=str(n)
	print('Skipped file: '+ filename)
	#########################
	# push to uid current uid
	# uid=UIDS(ufile=filename)
	# db.session.add(uid)
	# db.session.commit()
	global stat_B
	global stat_D
	global stat_filepath
	conn = mysql.connect()
	cursor = conn.cursor()
	if stat_B == 1:
		sql = "INSERT INTO bookmarks(file) VALUES(%s)"
		stat_B = 0
		data=(filename)
		cursor.execute(sql,data)
		conn.commit()
	elif stat_D == 1:
		sql = "INSERT INTO corrections(pfile,pfilepath) VALUES(%s,%s)"
		stat_D = 0
		data=(filename,stat_filepath)
		cursor.execute(sql,data)
		conn.commit()
	else:
		sql="INSERT INTO uids(ufile) VALUES(%s)"
		stat_B = 0
		data=(filename)
		cursor.execute(sql,data)
		conn.commit()

	#########################
	# remove in-process of this n in Info table
	# temp = Info.query.filter_by(file=filename,username=str(current_user.username)).first()
	# if temp:
	#     temp.status="skipped"
	#     db.session.commit()

	status="skipped"
	sql = "UPDATE info SET status=%s WHERE file=%s and username=%s"
	data = (status,filename,current_user.username)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, data)
	conn.commit()
	#########################

	time.sleep(1)


	emit('fetchNextResponse',str("skipped"))
	# else:
	#     # TODO: handle this exception
	#     emit('fetchNextResponse',str("none"))

################## handling file not found ########################
# reportBack function
@socketio.on('reportBack')
def reportBack(n):
	# emit('fetchNextResponse',str("skipped"))
	filename=str(n)
	print('Reported file: '+ filename)

	# delete from Image LInks
	conn = mysql.connect()
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	cursor.execute("DELETE FROM imagelinks WHERE file=%s;",filename)
	conn.commit()

	# delete from UID
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("DELETE FROM uids WHERE ufile=%s",filename)
	conn.commit()


	pathtoreportfile='home/dba/test/report.text'
	# keep the corrupted file in a text file
	with open(pathtoreportfile,'a') as f:
		f.write(filename)
	
	emit('fetchNextResponse',str("Reported"))
###################################################################
# fetchURL and send it back
@socketio.on('fetchURL')
def fetchURL(aid):

	#  added to request queue
	# caid=RequestUIDS(ruid=aid)
	# db.session.add(caid)
	# db.session.commit()
	print('AID: ',aid, 'Requesting: ')

	sql = "INSERT INTO ruids (ruid) VALUES(%s)"
	data = (aid)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, data)
	conn.commit()

	time.sleep(1)
	# Puppy.query.all()
	# aid=RequestUIDS.query.all()
	# if aid[0].ruid:
	#     db.session.delete(aid[0])
	#     db.session.commit()

	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("DELETE FROM ruids limit 1;")
	conn.commit()


	n=0
	# uids=UIDS.query.all()

	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT * from uids LIMIT 1;")
	rows = cursor.fetchone()
	conn.commit()

	# print("Allocated "+str(len(uids)))
	# print(random.randint(1,len(uids)))
	if rows:
		# n=randint(1,len(uids))
		# db.session.delete(uids[n])
		# db.session.commit()

		# SELECT * FROM uids ORDER BY RAND() LIMIT 1
		conn = mysql.connect()
		# cursor = conn.cursor()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		sql2 = "SELECT COUNT(*) FROM bookmarks;"
		cursor.execute(sql2)
		de = cursor.fetchone()
		de = de['COUNT(*)']
		print(de)
		global stat_B
		if de <= 0:
				cursor.execute("SELECT * FROM uids ORDER BY RAND() LIMIT 1;")
				uid = cursor.fetchone()
				conn.commit()
				filename=uid['ufile']
				stat_B = 0
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute("DELETE FROM uids WHERE ufile=%s",filename)
				uid = cursor.fetchone()
				conn.commit()
		else:
				cursor.execute("SELECT * FROM bookmarks ORDER BY RAND() LIMIT 1;")
				uid = cursor.fetchone()
				conn.commit()
				filename=uid['file']
				conn = mysql.connect()
				cursor = conn.cursor()
				cursor.execute("DELETE FROM bookmarks WHERE file=%s",filename)
				uid = cursor.fetchone()
				stat_B = 1
				conn.commit()

		

		# int(uids[0].uid)
		# filename=str(uids[n].ufile)
		print("Allocated filename "+filename)

		# imagelink=ImageLinks.query.filter_by(file=filename).first()
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM imagelinks WHERE file=%s LIMIT 1;",filename)
		imagelinks = cursor.fetchone()
		conn.commit()


		imagelink=str(imagelinks['links'])
		jsonfile={}
		# give file id ,not n
		jsonfile['file']=filename
		#jsonfile['imagelinks']="static/imgdata/" + str(imagelink[30:])
		jsonfile['imagelinks']=str(imagelink)
		data=json.dumps(jsonfile)
		print(type(data))

		# update the info table
		############# uncomment below ############
		status="in_process"
		dateOfAnnotation=time.ctime()
		# info=Info(str(current_user.username),filename,status,dateOfAnnotation,str(imagelink))
		# db.session.add(info)
		# db.session.commit()

		sql = "INSERT INTO info(username, file,status,date,localurl) VALUES(%s, %s, %s,%s,%s)"
		d = (str(current_user.username),filename,status,dateOfAnnotation,imagelink)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, d)
		conn.commit()


		emit('fetchURLResponse',str(data))
	else:
		# TODO: handle this exception
		emit('fetchURLResponse',str("none"))


@app.route('/')
def home():
	# TODO: show user their undone work and update info table(inprocess-undone)
	# temp=Info.query.filter_by(status="in_process")
	# undoneUID=[]
	# for i in temp:
	#     # print(i.uid)
	#     i.status="undone"
	#     uid=UIDS((i.file))
	#     db.session.add(uid)
	# else:
	#     db.session.commit()

	# sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
	in_process="in_process"
	undone="undone"
	sql = "UPDATE info SET status=%s WHERE status=%s"
	data = (undone,in_process)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, data)
	conn.commit()

	return render_template('home.html')


@app.route('/annotation')
@login_required
def annotationtool():

	# temp=Info.query.filter_by(status="in_process")
	# undoneUID=[]
	# for i in temp:
	#     # print(i.uid)
	#     i.status="undone"
	#     uid=UIDS((i.file))
	#     db.session.add(uid)
	# else:
	#     db.session.commit()

	in_process="in_process"
	undone="undone"
	sql = "UPDATE info SET status=%s WHERE status=%s"
	d = (undone,in_process)
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute(sql, d)
	conn.commit()

	# ndoc=Info.query.filter_by(username=current_user.username).count()

	conn = mysql.connect()
	cursor=conn.cursor(pymysql.cursors.DictCursor)

	cursor.execute("SELECT count(*) as n FROM info WHERE username=%s and status=%s",(current_user.username,"skipped"))
	n_skipped = (cursor.fetchone())['n']
	# print("Skipped "+str(n_skipped))

	cursor.execute("SELECT count(*) as n FROM info WHERE username=%s and status=%s",(current_user.username,"undone"))
	n_undone = (cursor.fetchone())['n']
	# print("Undone: "+ str(n_undone))

	cursor.execute("SELECT count(*) as n FROM info WHERE username=%s and status=%s",(current_user.username,"annotated"))
	n_annotated = (cursor.fetchone())['n']
	# print("Annotated: "+ str(n_annotated))

	cursor.execute("SELECT count(*) as n FROM info WHERE username=%s",(current_user.username))
	n_served = (cursor.fetchone())['n']
	# print("Doc Served: "+ str(n_served))

	# nundone=Info.query.filter_by(username=current_user.username,status="undone").count()
	# nskipped=Info.query.filter_by(username=current_user.username,status="skipped").count()
	# nannotated=Info.query.filter_by(username=current_user.username,status="annotated").count()
	# ,nskipped=nskipped,nannotated=nannotated,nundone=nundone,ndoc=ndoc

	pannotate=0
	pskipped=0
	pundone=0
	if n_served!=0:
		pannotate=n_annotated/n_served*100
		pannotate=round(pannotate,2)
		pskipped=n_skipped/n_served*100
		pundone=n_undone/n_served*100
		
	return render_template('annotationtool.html',aid=current_user.id,n_served=n_served,n_undone=n_undone,n_skipped=n_skipped,n_annotated=n_annotated,pundone=pundone,pannotate=pannotate,pskipped=pskipped)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	# unset the session
	# session.pop('uid_by_aid','not_set')
	flash('You logged out!')
	return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# Grab the user from our User Models table
		user = User.query.filter_by(email=form.email.data).first()

		# Check that the user was supplied and the password is right
		# The verify_password method comes from the User object
		# https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

		if user is not None and user.check_password(form.password.data):
			#Log in the user

			login_user(user)
			flash('Logged in successfully.')

			# If a user was trying to visit a page that requires a login
			# flask saves that URL as 'next'.
			next = request.args.get('next')

			# So let's now check if that next exists, otherwise we'll go to
			# the welcome page.
			if next == None or not next[0]=='/':
				next = url_for('annotationtool')

			return redirect(next)
	return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					password=form.password.data)

		db.session.add(user)
		db.session.commit()

		email=str(form.email.data)
		username=str(form.username.data)
		password=str(form.password.data)
		password=generate_password_hash(password)
		sql = "INSERT INTO users(email,username,password_hash) values(%s,%s,%s)"
		data = (email,username,password)
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()

		flash('Thanks for registering! Now you can login!')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

if __name__ == '__main__':
	# for i in range(1,792):
	#     t=UIDS(i)
	#     db.session.add(t)
	# db.session.commit()
	# db.create_all()
	# app.run(debug=True,host='10.5.0.142',port=12345)
	socketio.run(app,debug=True,host=sys.argv[5],port=10000)
	# socketio.set('transports', ['websocket']);
	# socketio.run(app)
