import mysql.connector as sql
conobject=sql.connect(host='localhost',user='root',passwd='1234',database='python')
cursor=conobject.cursor()
def putin(a,b,c,d):
     F='insert into phone_no(SNO,NAME,STATE,MOBILENO) VALUES({},"{}","{}","{}")'.format(a,b,c,d)
     cursor.execute(F)
     conobject.commit()
cursor.execute('CREATE TABLE phone_no(SNO int,NAME char(30),STATE char(30),MOBILENO char(20))')
putin(1,'Name','State','ph no')


