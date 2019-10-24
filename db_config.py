from app import app
from flaskext.mysql import MySQL

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASS'] = ''
app.config['MYSQL_DATABASE_DB'] = 'nce'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)