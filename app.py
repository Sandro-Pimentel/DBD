from flask import Flask, render_template, request
#from flask_mysqldb import MySQL

app = Flask('__name__')

# app.config['MySQL_HOST'] = 'localhost'
# app.config['MySQL_USER'] = 'gokuk'
# app.config['MySQL_PASSWORD'] = ''
# app.config['MySQL_DB'] = 'DeadbyDaylight'

# mysql = MySQL(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

