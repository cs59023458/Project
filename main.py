# Import
import os
from app import app
from flask import render_template, request, redirect, url_for
from flask import make_response, json, jsonify, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import UserMixin
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from forms import RegistrationForm, LoginForm
from calculate import Nutrients, Call
from sel import sel
from insertdata import ad
import numpy as np
import math

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# engine = create_engine(os.getenv("DATaBASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))

# Home Page
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/calculate")
def calculate():
    food = sel.select_food('self')
    datap = sel.select('p')
    datac = sel.select('c')
    dataf = sel.select('f')
    return render_template('calculatecalories.html', p=datap, c=datac, f=dataf, food=food)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/calendar")
def calendar():
    return render_template('calendar.html')


@app.route("/process", methods=['POST'])
def process():
    a = request.form['a']
    name = sel.select_food_name(a)
    pro = request.form['pro']
    car = request.form['car']
    fat = request.form['fat']
    # ปริมาณที่รับมาจาก slider ------------------------
    volumep = request.form['volumep']  # str
    volumec = request.form['volumec']
    volumef = request.form['volumef']
    volp = float(volumep)
    volc = float(volumec)
    volf = float(volumef)
    # ----------------------------------------------
    # ปริมาณต่อ 100 g +++++++++++++++++++++++++++++++
    P = sel.select_nutrients(pro)
    C = sel.select_nutrients(car)
    F = sel.select_nutrients(fat)
    # ++++++++++++++++++++++++++++++++++++++++++++++
    # ปริมาณจริงของสารอาหารแต่ละตัว ####################
    ValP = Call.Calculate(volp, P)  # ปริมาณของ  p c f จริง
    ValC = Call.Calculate(volc, C)
    ValF = Call.Calculate(volf, F)
    ################################################
    # พลังงานของสารอาหารแต่ละตัว ----------------------
    EnP = Call.Total_Calculate(ValP)
    EnC = Call.Total_Calculate(ValC)
    EnF = Call.Total_Calculate(ValF)
    # พลังงานของรวมของ P C F ในแต่ละตัว
    E1 = math.ceil(EnP.sum())
    E2 = math.ceil(EnC.sum())
    E3 = math.ceil(EnF.sum())
    # ----------------------------------------------
    # พลังงานทั้งหมด +++++++++++++++++++++++++++++++++
    En = math.ceil(Call.Energy(EnP, EnC, EnF))  # เก็บลง databasc
    # ++++++++++++++++++++++++++++++++++++++++++++++
    return jsonify({"pro": E1, "car": E2, "fat": E3, "En": En})
# return jsonify({'V1': 'V1', 'V2': 'V2', 'V3': 'V3', 'EnP': 'EnP', 'EnC': 'EnC', 'EnF': 'EnF', 'En': 'En'})

@app.route("/addfood", methods=['POST'])
def addfood():
    a = request.form['a']
    pro = request.form['pro']
    car = request.form['car']
    fat = request.form['fat']
    name1 = sel.select_food_name_a(a)
    name2 = sel.select_food_name_b(pro)
    name3 = sel.select_food_name_b(car)
    name4 = sel.select_food_name_b(fat)
    name5 = name3+name1+name2+name4
    # ปริมาณที่รับมาจาก slider ------------------------
    volumep = request.form['volumep']  # str
    volumec = request.form['volumec']
    volumef = request.form['volumef']
    volp = float(volumep)
    volc = float(volumec)
    volf = float(volumef)
    # ----------------------------------------------
    # ปริมาณต่อ 100 g +++++++++++++++++++++++++++++++
    P = sel.select_nutrients(pro)
    C = sel.select_nutrients(car)
    F = sel.select_nutrients(fat)
    # ++++++++++++++++++++++++++++++++++++++++++++++
    # ปริมาณจริงของสารอาหารแต่ละตัว ####################
    ValP = Call.Calculate(volp, P)  # ปริมาณของ  p c f จริง
    ValC = Call.Calculate(volc, C)
    ValF = Call.Calculate(volf, F)
    ################################################
    # พลังงานของสารอาหารแต่ละตัว ----------------------
    EnP = Call.Total_Calculate(ValP)
    EnC = Call.Total_Calculate(ValC)
    EnF = Call.Total_Calculate(ValF)
    # พลังงานของรวมของ P C F ในแต่ละตัว
    E1 = math.ceil(EnP.sum())
    E2 = math.ceil(EnC.sum())
    E3 = math.ceil(EnF.sum())
    # ----------------------------------------------
    # พลังงานทั้งหมด +++++++++++++++++++++++++++++++++
    En = math.ceil(Call.Energy(EnP, EnC, EnF))  # เก็บลง databasc
    # ++++++++++++++++++++++++++++++++++++++++++++++
    ad.addfood(name5,ValP,ValC,ValC,EnP,EnC,EnF,E1,E2,E3,En)
    return jsonify({"A": "Add Food"})

@app.route("/foodtable")
def fkoodtable():
    return render_template('foodtable.html')


@app.route("/his")
def his():
    food = sel.select_food('self')
    return render_template('his.html', foods=food)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        E = request.form['email']
        if request.form['password'] == 'password':
            return redirect(url_for('home'))

    return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')


'''
# Calculate
@app.route("/calculate")
def calculate():
    with conn1:
        cur = conn1.cursor()
        cur.execute("""SELECT *
        FROM  nutrients 
        WHERE nutrients_group = '2'""")
        rowsp = cur.fetchall()
    with conn1:
        cur = conn1.cursor()
        cur.execute("""SELECT *
        FROM  nutrients 
        WHERE nutrients_group = '1'""")
        rowsc = cur.fetchall()
    with conn1:
        cur = conn1.cursor()
        cur.execute("""SELECT *
        FROM  nutrients 
        WHERE nutrients_group = '3'""")
        rowsf = cur.fetchall()
    with conn1:
        cur = conn1.cursor()
        cur.execute("""SELECT id_calculationtype,type
                    FROM foodcalculationtype""")
        row = cur.fetchall()
    return render_template('cal.html',data=row,datap=rowsp,datac=rowsc,dataf=rowsf)

# Table
@app.route("/table")
def table():
    return render_template('table.html')

# add data member page
@app.route("/member")
def addmember():
    return render_template('add_member.html',)

# Manage Accounts Page
@app.route("/manage")
def manage():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM member")
        rows = cur.fetchall()
    return render_template('manage.html',datas=rows)

# Delete Data Function Manage
@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM member WHERE id=%s",(id_data))
        conn.commit()
    return redirect(url_for('manage'))

# Update Data Function Manage
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

# Insert Member Data
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

# Show Foods Page

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

# Show Ingedients 
@app.route("/showingedients")
def showingedients():
    with conn1:
        cur = conn1.cursor()
        cur.execute("""
        SELECT * FROM `nutrients` LIMIT 10""")
        rows = cur.fetchall()
    return render_template('ingedients.html', data_in=rows, title='Ingedients')

# Add Ingedients Page
@app.route("/showingedients/ingedients")
def addIngedients():
    return render_template('add_ingedients.html')


# Insert Ingedients Data
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
        return redirect(url_for('ingedients'))'''

# Debug Code
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=8000)
