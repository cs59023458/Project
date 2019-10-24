#Import
import os   
from app import app
from flask import render_template, request, redirect, url_for, jsonify, session, make_response, json
from flask_mysqldb import MySQL
from forms import RegistrationForm, LoginForm
from calculate import Nutrients, Call
from sel import sel
import numpy as np

# Home Page
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calculate")
def calculate():
    if request.method == 'GET':
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
    if request.method == 'POST':
        a = request.form.get('foodname', type=str)
        name = sel.select_food_name(a)
        pro = request.form.get('P', type=str)  # str
        car = request.form.get('C')
        fat = request.form.get('F')
        # ปริมาณที่รับมาจาก slider ------------------------
        volumep = int(request.form.get('volumep'))  # str
        volumec = int(request.form.get('volumec'))
        volumef = int(request.form.get('volumef'))
        # ----------------------------------------------
        # ปริมาณต่อ 100 g +++++++++++++++++++++++++++++++
        P = list(sel.select_nutrients(pro))  # tuple
        C = list(sel.select_nutrients(car))
        F = list(sel.select_nutrients(fat))
        # ++++++++++++++++++++++++++++++++++++++++++++++
        # ปริมาณจริงของสารอาหารแต่ละตัว ####################
        ValP = list(Call.Calculate(volumep, P))  # ปริมาณของ  p c f จริง
        ValC = list(Call.Calculate(volumec, C))
        ValF = list(Call.Calculate(volumef, F))
        V1 = np.asanyarray(ValP)
        V2 = np.asanyarray(ValC)
        V3 = np.asanyarray(ValF)
        ################################################
        # พลังงานของสารอาหารแต่ละตัว ----------------------
        EnP = Call.Total_Calculate(ValP)
        EnC = Call.Total_Calculate(ValC)
        EnF = Call.Total_Calculate(ValF)
        E1 = EnP.sum()
        E2 = EnC.sum()
        E3 = EnF.sum()
        # ----------------------------------------------
        # พลังงานทั้งหมด +++++++++++++++++++++++++++++++++
        En = Call.Energy(EnP, EnC, EnF)
        # ++++++++++++++++++++++++++++++++++++++++++++++
        return jsonify({'data': render_template('calculatecalories.html',V1=V1.sum(),V2=V2.sum(),V3=V3.sum(),En=En,EnP=EnP,EnC=EnC,EnF=EnF)})

@app.route("/his")
def his():
    food = sel.select_food('self')
    return render_template('his.html', foods=food)


'''
#Calculate
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
        return redirect(url_for('ingedients'))'''

# Debug Code
if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port=8000)