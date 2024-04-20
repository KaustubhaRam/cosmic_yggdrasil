import cx_Oracle
from flask import Flask, render_template, request, session, request, jsonify
from werkzeug.utils import secure_filename
from flask.json import jsonify

app = Flask(__name__)
app.secret_key = 'pass'

con = cx_Oracle.connect('system/mysql@localhost:1521/xe')
cursor = con.cursor()

@app.route('/')
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM Starborn_Login WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['password'] = account['password']
            session['username'] = account['username']
            return render_template('home.html', user=session['username'])
    return render_template('login.html')