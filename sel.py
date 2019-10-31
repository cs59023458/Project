import pymysql
from db_config import mysql
import json

class sel:

    def select(self):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_nutrients,name_nutrients FROM nutrients WHERE group_nutrients = %s",(self))
        data = cursor.fetchall()
        return data

    def select_food(self):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id_food,name_food FROM Food")
        data = cursor.fetchall()
        return data

    def select_nutrients(self):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT protein_nutrients,carbohydrate_nutrients,fat_nutrients FROM nutrients WHERE id_nutrients = %s"%(self))
        data = cursor.fetchall()
        return data

    def select_food_name(self):
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name_food FROM Food WHERE id_food = %s"%(self))
        data = cursor.fetchall()
        return data

    #def insert():
     #   cur = mysql.connection.cursor()
      #  cur.execute("INSERT INTO `member` (`fname`,`lname`,`phone`) values(%s,%s,%s)")
