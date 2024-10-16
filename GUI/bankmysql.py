import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("show database")
for x in cursor:
    print(x)