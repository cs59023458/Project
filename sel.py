from db_config import mysql


class sel:

    def select(self):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT id_nutrients,name_nutrients FROM nutrients WHERE group_nutrients = %s", (self))
        data = cur.fetchall()
        return data

    def select_food(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT id_food,name_food FROM Food")
        data = cur.fetchall()
        return data

    def select_nutrients(self):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT protein_nutrients,carbohydrate_nutrients,fat_nutrients FROM nutrients WHERE id_nutrients = %s" % (self))
        row = cur.fetchone()
        data = []
        data.append(row['protein_nutrients'])
        data.append(row['carbohydrate_nutrients'])
        data.append(row['fat_nutrients'])
        return data

    def select_food_name(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT name_food FROM Food WHERE id_food = %s" % (self))
        data = cur.fetchall()
        return data

    def select_food_name_a(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT name_food FROM Food WHERE id_food = %s" % (self))
        row = cur.fetchone()
        data = row['name_food']
        return data

    def select_food_name_b(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT name_nutrients FROM Nutrients WHERE id_nutrients = %s" % (self))
        row = cur.fetchone()
        data = row['name_nutrients']
        return data

    def select_food_table(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT calculate_id,calculate_name,en_all FROM Calculate  WHERE calculate_meal = %s"%(self))
        row = cur.fetchall()
        return row
    
