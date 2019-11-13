from db_config import mysql


class addData:

    def addfood(self, name, a, b, c, d, e, f, g, h, i, j):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO calculate (calculate_name,val_protein_p,val_protein_c,val_protein_f,val_carbonide_p,val_carbonide_c,val_carbonide_f,val_fat_p,val_fat_c,val_fat_f,en_protein_p,en_protein_c,en_protein_f,en_carbonide_p,en_carbonide_c,en_carbonide_f,en_fat_p,en_fat_c,en_fat_f,en_p,en_c,en_f,en_all) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name, a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2], d[0], d[1], d[2], e[0], e[1], e[2], f[0], f[1], f[2], g, h, i, j))
        mysql.connection.commit()


ad = addData()
