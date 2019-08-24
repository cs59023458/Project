#Import
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import pymysql
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

#connect to DB
conn = pymysql.connect('localhost','root','','memberdb')
conn1 = pymysql.connect('localhost','root','','fooddb')

#Home Page
@app.route("/")
def index():
    return render_template('index.html')

#Login Page
@app.route("/login")
def login():
    return render_template('login.html')

#Register Page
@app.route("/register")
def register():
    return render_template('register.html')

#Forgot-Password page
@app.route("/forgotpassword")
def forgotpassword():
    return render_template('forgotpassword.html')

#404 page
@app.route("/404")
def error404():
    return render_template('404.html')

#About Page
@app.route("/about")
def about():
    return render_template('about.html')

#Calculate
@app.route("/calculate")
def calculate():
    return render_template('calculate.html')

#Table
@app.route("/table")
def table():
    return render_template('table.html')

#add data member page
@app.route("/member")
def addmember():
    return render_template('add_member.html',)

#Manage Accounts Page
@app.route("/manage")
def manage():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM member")
        rows = cur.fetchall()
    return render_template('manage.html',datas=rows)

#Delete Data Function Manage
@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM member WHERE id=%s",(id_data))
        conn.commit()
    return redirect(url_for('manage'))

#Update Data Function Manage
@app.route("/update",methods=['POST'])
def update():
    if request.method=="POST":
        id_update = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql = "UPDATE member SET fname=%s,lname=%s,phone=%s WHERE id=%s"
            cursor.execute(sql,(fname,lname,phone,id_update))
            conn.commit()
        return redirect(url_for('manage'))

#Insert Member Data
@app.route("/insert",methods=['POST'])
def insert():
    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql = "INSERT INTO `member` (`fname`,`lname`,`phone`) values(%s,%s,%s)"
            cursor.execute(sql,(fname,lname,phone))
            conn.commit()
        return redirect(url_for('manage'))    

#Show Foods Page
@app.route("/foods")
def showfood():
    with conn1:
        cur = conn1.cursor()
        cur.execute("""SELECT f.food_id, f.food_name,n1.ingredients_name,n2.ingredients_name,
        n3.ingredients_name 
        FROM foods f 
        INNER JOIN nutrients n1 ON f.ingredients_p = n1.ingredients_id 
        INNER JOIN nutrients n2 ON f.ingredients_c = n2.ingredients_id 
        INNER JOIN nutrients n3 ON f.ingredients_f = n3.ingredients_id""")
        rows = cur.fetchall()
    return render_template('foods.html',data=rows)

#Show Ingedients 
@app.route("/showingedients")
def showingedients():
    with conn1:
        cur = conn1.cursor()
        cur.execute("""
        SELECT * FROM `nutrients` LIMIT 10""")
        rows = cur.fetchall()
    return render_template('ingedients.html', data_in=rows, title='Ingedients')

#Add Ingedients Page
@app.route("/showingedients/ingedients")
def addIngedients():
    return render_template('add_ingedients.html')


#Insert Ingedients Data
@app.route("/insert_ingedients",methods=['POST'])
def insert_ingedients():
    if request.method=="POST":
        ingedients_name = request.form['ingedients_name']
        nutrients_group = request.form['nutrients_group']
        p = request.form['p']
        c = request.form['c']
        f = request.form['f']
        with conn1.cursor() as cursor:
            sql = """INSERT INTO `nutrients` 
            (`nutrients_group`, `ingredients_name`, `p`, `c`, `f`) 
            VALUES ('%s','%s','%s','%s','%s');"""
            cursor.execute(sql,(ingedients_name,nutrients_group,p,c,f))
            conn1.commit()
        return redirect(url_for('ingedients'))

#Debug Code
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost',port=8000)