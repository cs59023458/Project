from app import app
from flask_mysqldb import MySQL

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'nce'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)