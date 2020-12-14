from flask import Flask, request, render_template
import pyrebase
import datetime

config = {
  "apiKey": "AIzaSyANS18NvbjWWwx1JgRxAdWu4CmZzEdVtxM",
  "authDomain": "attendence-app-2d992.firebaseapp.com",
  "databaseURL": "https://attendence-app-2d992-default-rtdb.firebaseio.com/",
  "storageBucket": "attendence-app-2d992.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)




@app.route('/',methods=['POST','GET'])   
def result():
    if request.method =='POST':
        if request.form['submit'] == 'submit':
             x = datetime.datetime.now()
             x = x.strftime("%Y-%m-%d %H:%M:%S")
             
             name = request.form.get('name')
             contact = request.form.get('cn')
             roll = request.form.get('rn')
             university = request.form.get('un')
             
             print(name,contact,roll,university)

             payload = {'time' : x, 'Name' : name, 'ContactNo' : contact, 'RollNo' : roll, 'UniversityNo' : university}

             db.child('teachbotattendance').push(payload) 

             return render_template('index.html',submit = True,name = payload['Name'])
    return render_template('index.html', submit = False)

if __name__ == "__main__":
    app.run(debug = True)