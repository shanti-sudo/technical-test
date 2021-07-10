from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'anonymous'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'ensembl_website_102'
app.config['MYSQL_DATABASE_HOST'] = 'ensembldb.ensembl.org'
mysql.init_app(app)