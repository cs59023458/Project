import pymysql
connection = pymysql.connect('localhost','root','','nce')
cursor = connection.cursor()
sql_query = "SELECt VERSION()"

'''from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:''@localhost/nce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class nutrientsgroup(db.Model):
    __tablename__ = 'nutrientsgroup'
    #id = db.Column('id_group',db.String(255),primary_key=True)
    #name = db.Column('name_group',db.Text)

#connect to DB
class con():
    conn = pymysql.connect('localhost','root','','nce_member')
    conn1 = pymysql.connect()

Connect = con()

if __name__ == "__main__":
    manager.run()'''