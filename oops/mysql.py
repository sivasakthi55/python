import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("create database sivadata57")
cursor.execute("show databases")
for x in cursor:
    print(x)

cursor.execute("use sivadata57")
cursor.execute("create table departments(department_id int primary key,department_name varchar(50))")
cursor.execute("show tables")
print("number of table in database:")
for x in cursor:
    print(x)

s="insert into departments values(%s,%s)"
t=(2,"siva")
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted",cursor.lastrowid) 
cursor.execute("select * from departments")
result=cursor.fetchall()
print("Content in the python :")
for x in result:
   print("\t",x)

sql="update departments set department_name='bala' where department_id=1;"
cursor.execute(sql)
connection.commit()
cursor.execute("select * from departments")
result=cursor.fetchall()
print("content in the python:")
for x in result:
    print("\t",x)

sql="delete from departments where department_id=1;"
cursor.execute(sql)
connection.commit()
print(cursor.rowcount,"record(s) delect")
cursor.execute("select * from departments")
result=cursor.fetchall()
print("content in the python:")
for x in result:
    print("\t",x)