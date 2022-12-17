import pyrebase
conf={"apiKey": "AIzaSyDTC-5rT772RoHvK050Tzo0LmWS2UL2i10",
  "authDomain": "fir-demo-656dd.firebaseapp.com",
  "projectId": "fir-demo-656dd",
  "storageBucket": "fir-demo-656dd.appspot.com",
 " messagingSenderId": "570748775242",
 "databaseURL":"https://fir-demo-656dd-default-rtdb.firebaseio.com/",
 " appId": "1:570748775242:web:26898e9c4998a1adfa2fb3",
 " measurementId": "G-6WVT7ERM13"}
firebase=pyrebase.initialize_app(conf)
database=firebase.database()
data={"Age":21,"Name":"Alok","Likes Pizza":True}
database.push(data)
print("done")