import cx_Oracle
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'pass'

con = cx_Oracle.connect('system/mysql@localhost:1521/xe')
cursor = con.cursor()



@app.route('/', methods=['GET', 'POST'])  # Accept both GET and POST requests
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        # Correct SQL query parameterization using ":" instead of "%s"
        cursor.execute('SELECT * FROM Starborn_Login WHERE username = :username AND password = :password', 
                       {'username': username, 'password': password})
        row = cursor.fetchone()
        print(row)
        if row:
            # Extract column names from cursor description
            column_names = [desc[0] for desc in cursor.description]
            # Create a dictionary mapping column names to values
            account = dict(zip(column_names, row))
            print(account)
            session['loggedin'] = True
            session['password'] = account['PASSWORD']
            session['username'] = account['USERNAME']
            return render_template('home.html', user=session['username'])
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/agencies')
def agencies():
    return render_template('agencies.html')

@app.route('/budget')
def budget():
    return render_template('budget.html')

@app.route('/exoplanets')
def exoplanets():
    return render_template('exoplanets.html')

@app.route('/planets')
def planets():
    return render_template('planets.html')

@app.route('/spacecrafts')
def spacecrafts():
    return render_template('spacecrafts.html')

@app.route('/stars')
def stars():
    return render_template('stars.html')


if __name__ == "__main__":
    app.run(debug=True)
