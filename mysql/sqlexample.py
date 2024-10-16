import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
"""cursor.execute("show databases")
for x in cursor:
    print(x)"""
cursor.execute("use sivadata57")
cursor.execute("show tables")
print("number of table in database:")
for x in cursor:
    print(x)
    
print(cursor.rowcount,"new row inserted",cursor.lastrowid) 
cursor.execute("select * from departments")
result=cursor.fetchall()
print("Content in the python :")
for x in result:
   print("\t",x)

"""s="insert into departments values(%s,%s)"
t=(3,"sivall")
cursor.execute(s,t)
connection.commit()

s="insert into departments values(%s,%s)"
t=(1,"kumar")
cursor.execute(s,t)
connection.commit()"""