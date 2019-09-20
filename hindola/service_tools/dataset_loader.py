import sys
import os
import mysql.connector

# second argument -> mysql username
# third argument -> path to where collections are

arg1 = str(sys.argv[1])
arg2 = str(sys.argv[2])
arg3 = str(sys.argv[3])
arg4 = str(sys.argv[4])
arg5 = '/data'


mydb = mysql.connector.connect(
  host=str(arg4),
  user=str(arg1),
  passwd=str(arg2),
  database=str(arg3)
)

mycursor = mydb.cursor()

foldernames = []
for foldername in os.listdir(arg5):
	print(foldername)
	prefix = input("Enter prefix for collection " + str(foldername) +  " (size should be <= 6): ")
	while len(prefix) > 6:
		prefix = input("You entered a prefix greater than six characters. Please enter a prefix for collection " + str(foldername) + " size should be <= 6: ")
	temp = {}
	temp['name'] = str(foldername)
	temp['prefix'] = str(prefix)
	foldernames.append(temp)

imagelinks = []

def rec(path):
	for item in os.scandir(path):
		if item.is_dir():
			new_path = str(str(path) + "/" + str(item.name))
			rec(new_path)
		else:
			temp = {}
			s = path + "/" + str(item.name)
			temp['filename'] = str(str(folder['prefix']) + "-" + str(hash(s)))
			temp['url'] = s
			imagelinks.append(temp)

for folder in foldernames:
	booknames = os.listdir(str(arg5) + "/" + str(folder['name']))
	for item in booknames:
		path = str(str(arg5) + "/" + str(folder['name']) + "/" + str(item))
		rec(path)
		
for item in imagelinks:
	# print(str(item['filename']) + ": " + str(item['url']))
	actual_path = item['url']
	#actual_path = sys.argv[5] + actual_path[5:]
	actual_path = 'main/myproject/static/imgdata' + actual_path[5:]
	sql = "INSERT INTO imagelinks (file, links) VALUES (%s, %s);"
	val = (item['filename'],actual_path)
	mycursor.execute(sql, val)
	mydb.commit()
	sql = "INSERT INTO uids (ufile) VALUES (%s);"
	val = (item['filename'],)
	mycursor.execute(sql, val)
	mydb.commit()