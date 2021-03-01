from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

# Подключение к БД, необходимо записать в конфиг приложения данные для использования БД
app.config['MYSQL_DATABASE_HOST'] = 'AdmLangley.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'AdmLangley'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Zanyat1221'
app.config['MYSQL_DATABASE_DB'] = 'AdmLangley$hrdep_db'

# Создаем объект с импортированной библиотеки и заносим туда наше app с Flask
mysql = MySQL()
mysql.init_app(app)