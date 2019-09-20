def select_from_collection(collection):

	print(collection)
	# select_from_collection('name')
    n=0
    # uids=UIDS.query.all()

    conn = mysql.connect()
    cursor = conn.cursor()
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
        urls=imgLinks['links']
		print(urls)
		emit('fetchURLResponse',str("none"))
        # stat_B = 0

		

        # int(uids[0].uid)
        # filename=str(uids[n].ufile)
        # print("Allocated filename "+filename)

        # imagelink=ImageLinks.query.filter_by(file=filename).first()


        # imagelink=str(imagelinks['links'])
        # jsonfile={}
        # # give file id ,not n
        # jsonfile['file']=filename
        # jsonfile['imagelinks']=str(imagelink)
        # data=json.dumps(jsonfile)
        # print(type(data))

        # emit('fetchURLResponse',str(data))
    else:
        # TODO: handle this exception
        emit('fetchURLResponse',str("none"))
