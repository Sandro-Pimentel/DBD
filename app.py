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

@app.route('/shrine')

def shrine():
    return render_template('shrine.html')

@app.route('/survs')

def survs():
    return render_template('survs.html')

@app.route('/killers')

def killers():
    return render_template('killers.html')

@app.route('/maps')

def maps():
    return render_template('maps.html')