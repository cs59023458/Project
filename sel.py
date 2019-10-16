from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "flash message"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'nce'

mysql = MySQL(app)

class sel:

    def select(self):
        a = mysql.connection.cursor()
        a.execute("SELECT id_nutrients,name_nutrients FROM nutrients WHERE group_nutrients = %s",(self))
        data = a.fetchall()
        a.close()
        return data

    def select_food(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT id_food,name_food FROM Food ")
        data1 = cur.fetchall()
        cur.close()
        return data1

    def select_nutrients(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT protein_nutrients,carbohydrate_nutrients,fat_nutrients FROM nutrients WHERE id_nutrients = %s"%(self))
        data2 = cur.fetchall()
        cur.close()
        return data2

    def select_food_name(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT name_food FROM Food WHERE id_food = %s"%(self))
        data = cur.fetchall()
        cur.close()
        return data


    #def insert():
     #   cur = mysql.connection.cursor()
      #  cur.execute("INSERT INTO `member` (`fname`,`lname`,`phone`) values(%s,%s,%s)")
