import pymysql
bd=pymysql.connect(host="localhost",user="root", passwd="root",db="ORSYS_FORMATION_PYTHON")

cursor=bd.cursor(pymysql.cursors.DictCursor)

cursor.execute("SELECT * FROM contact")

for result in cursor.fetchall():
    print(result)