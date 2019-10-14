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
        cur = mysql.connection.cursor()
        cur.execute("SELECT id_nutrients,name_nutrients FROM nutrients WHERE group_nutrients = %s",(self))
        data = cur.fetchall()
        cur.close()
        return data

    def select1():
        cur = mysql.connection.cursor()
        cur.execute("SELECT id_food,name_food FROM food ")
        data1 = cur.fetchall()
        cur.close()
        return data1

    #def insert():
     #   cur = mysql.connection.cursor()
      #  cur.execute("INSERT INTO `member` (`fname`,`lname`,`phone`) values(%s,%s,%s)")
