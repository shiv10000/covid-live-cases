import mysql.connector as sqltor

from twilio.rest import Client
import requests
cobject=sqltor.connect(host="localhost",user="root",passwd="1234",database="python")
cursor=cobject.cursor()
cursor.execute('select* from PHONE_NO')
a=''
while a!=None:
 a=cursor.fetchone()
 if a==None:
   print('Messaage Sent')
   continue
 def name():
  name=a[1]
  return name
 def state():
    state=a[2]
    return state
 def mobileno():
    mobile=a[3]
    return mobile
 statecode={'MAHARASHTRA':1,'KERALA':2,'KARNATAKA':3,'ANDHRA PRADESH':4,
 'Tamil Nadu':5,'Delhi':6,'U.P':7,'WEST BENGAL':8,'ODISHA':9}
 def active():
  stat=state()
  code=statecode[stat]
  a=requests.get('https://api.covid19india.org/data.json')
  c=a.json()
  act=''
  for i in c['statewise'][code]['active']:
    act=act+str(i)
  return act
 def confirmed():
  stat=state()
  code=statecode[stat]
  a=requests.get('https://api.covid19india.org/data.json')
  c=a.json()
  conf=''
  for i in c['statewise'][code]['confirmed']:
    conf=conf+str(i)
  return conf
 def deaths():
  stat=state()
  code=statecode[stat]
  a=requests.get('https://api.covid19india.org/data.json')
  c=a.json()
  deat=''
  for i in c['statewise'][code]['deaths']:
    deat=deat+str(i)
  return deat
 def recovered():
  stat=state()
  code=statecode[stat]
  a=requests.get('https://api.covid19india.org/data.json')
  c=a.json()
  recov=''
  for i in c['statewise'][code]['recovered']:
    recov=recov+str(i)
  return recov
 sid = "Frome twillo write"
 token = "From twillo write"
 
 client = Client(sid, token)
 
 message = client.messages.create(
     to = mobileno(),# put your registered twilio number here
     from_ = "Ph no from twillo",
     body = 'HLO'+' '+name()+' '+"." +
     'IN your state'+' '+
     state()+' '+'active cases'+
     '-'+active()+
     ' ,'+'confirmed'+'-'+confirmed()+
     ','+ 'recovered'+'-'+recovered()+
     ','+'deaths'+'-'+deaths()+
     " "+'in order to avoid covid19 follow the'+" "+
     'provided guidelines and stay home and stay safe'      
     )
 
 print(message.sid)
































