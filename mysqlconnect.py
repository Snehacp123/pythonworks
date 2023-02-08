# import pymysql
# db = pymysql.connect(host='localhost',user='root',password='Snehacp@123',database='nev_test')
# con = db.cursor()
# sqlquery = 'insert into t1 values(%s,%s,%s)'
# val = (16,'anju',25)
# con.execute(sqlquery,val)
# db.commit()
# print('inserted')

# to insert user input values

# import pymysql
# id = int(input("enter the id:"))
# name = input("enter the name:")
# age = int(input("enter the age:"))
# db = pymysql.connect(host='localhost',user='root',password='Snehacp@123',database='nev_test')
# mycursor = db.cursor()
# sql = 'insert into t1 values(%s,%s,%s)'
# val = (id,name,age)
# mycursor.execute(sql,val)
# db.commit()
# print("inserted successfully")

# to delete an value

# import pymysql
# id = int(input("enter the id:"))
# db = pymysql.connect(host='localhost',user='root',password='Snehacp@123',database='nev_test')
# mycursor = db.cursor()
# sql = "delete from t1 where id='%d' "%(id)
# mycursor.execute(sql)
# db.commit()
# print("delete successfully")

# to update
# import pymysql
# y = input("Do you want to update?")
# if y == 'yes':
#     db = pymysql.connect(host='localhost',user='root',password='Snehacp@123',database='nev_test')
#     id = int(input("enter the id:"))
#     name = input("enter the name:")
#     age = int(input("enter the age:"))
#     c= db.cursor()
#     sql = "update t1 set name='%s' ,age='%d' where id='%d' "%(name,age,id)
#     c.execute(sql)
#     db.commit()
# elif y == 'no' :
#     print('exit')
# print("update successfully")

# fetch details

# import pymysql
# id = int(input("enter the id:"))
# db = pymysql.connect(host='localhost',user='root',password='Snehacp@123',database='nev_test')
# con = db.cursor()
# sql = "select * from t1 where id = %d" %id
# con.execute(sql)
# i = con.fetchone()
# id = i[0]
# name = i[1]
# age = i[2]
# print(f'id = {i[0]},name = {name},age = {age}')

# fetch all
import pymysql
db = pymysql.connect(host='localhost',user='root',password='Snehacp@123',database='nev_test')
con = db.cursor()
sql = "select * from t1 "
con.execute(sql)
data = con.fetchall()
for i in data:
    id = i[0]
    name = i[1]
    age = i[2]
    print(f'id = {i[0]},name = {name},age = {age}')











