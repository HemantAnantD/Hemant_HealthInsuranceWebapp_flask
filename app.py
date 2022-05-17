from ast import If
from re import A
from select import select
from flask import Flask,render_template,request,session,redirect
from dbms import *
import pymysql as p

app = Flask(__name__)
app.secret_key="abc"

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='ins')

@app.route("/")
def home_func():
  return render_template("home.html")

@app.route("/aboutlink")
def about_func():
    return render_template("about.html")

@app.route("/savelink",methods=["POST"])
def about_save():
    return redirect("aboutlink")
  
@app.route("/reglink")
def register_func():
      return render_template("register.html")


@app.route("/savelink2",methods=["POST"])
def save_func():
    name=request.form['name']
    password=request.form['password']
    Age=request.form['Age']
    Mobilenumber=request.form['MobileNumber']
    email=request.form['email']
    t=(name,password,Age,Mobilenumber,email)
    addData(t)
    return redirect("reglink")
    

@app.route("/loginlink")
def login_func():
    return render_template("login.html")


@app.route("/savelink3",methods=["POST"])
def login_save():
    if request.method=='POST' and 'name' in request.form and 'password' in request.form:
        username=request.form['name']
        password=request.form['password']
        con=getConnection()
        cur=con.cursor()
        cur.execute("select * from ins_s where name=% s AND password=% s",(username,password) )
        result=cur.fetchone()
        if result:
            session['k']=True

            return redirect("informationlink")
        
        else:
            return "<h1> Enter correct usernsme and password...."

    
    

@app.route("/logoutlink")
def logout_func():
    session.pop('name',None)
    session.pop('password',None)
    return "<h1> Logout Successful </h1>"



@app.route("/informationlink")
def information_func():
    return render_template("information.html")

@app.route("/savelink4",methods=["POST"])
def information_save():
    if request.method=='POST':
        name=request.form['name']
        Age=request.form['Age']
        choosefor=request.form['choosefor']
        coverage=request.form['coverage']
        premium_oneyear=(int(Age)*int(choosefor)*int(coverage))/2000
        return render_template("premium.html",premium=premium_oneyear)

@app.route("/premiumlink")
def premium_func():
    return render_template("premium.html")

@app.route("/savelink5",methods=["POST"])
def premium_save():
    return redirect("premium.html")


@app.route("/detail1link")
def detail1_func():
    return render_template("detail1.html")

@app.route("/detail2link")
def detail2_func():
    return render_template("detail2.html")

@app.route("/detail3link")
def detail3_func():
    return render_template("detail3.html")


@app.route("/displaylink")
def display_func():
    datalist=fetchData()
    return render_template("display.html",data=datalist)

@app.route('/editlink/<int:id>')
def displayforupdate(id):
    datalist=specificdata(id)
    return render_template('edit.html',data=datalist)

@app.route('/updatelink/<int:id>',methods=["POST"])
def updatefun(id):
    name=request.form['name']
    password=request.form['password']
    Age=request.form['Age']
    Mobilenumber=request.form['MobileNumber']
    email=request.form['email']
    t=(name,password,Age,Mobilenumber,email)
    updatedata(t)
    return redirect("/displaylink")

@app.route("/deletelink/<int:id>")
def deletefun(id):
    deletedata(id)
    return redirect("/displaylink") 

    
if __name__ == '__main__':
  app.run(debug=True)