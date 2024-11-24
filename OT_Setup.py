#one-time steup

import mysql.connector as sql
con=sql.connect(host='localhost',user='root')
cur=con.cursor()

cur.execute('create database if not exists anthony')
cur.execute('use anthony')

qry2='''create table if not exists query
          (Query_Box varchar(500)
          )'''

cur.execute(qry2)


qry='''create table if not exists user_dat
           ( Name varchar(50),
           UName varchar(30),
           UPass varchar(8),
           Email varchar(20),
           Mobile char(13),
           Gender varchar(7),
           DOB date
           )'''

cur.execute(qry)

cur.execute("select * from user_dat where UName='admin1'")
data=cur.fetchall()
if cur.rowcount <1:
    rec='''insert into user_dat
           values(1,'admin1','admin','dbowner@gmail.com','+919000000000','2007/05/18','Male')
        '''
    cur.execute(rec)
    con.commit()
