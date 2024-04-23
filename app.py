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
    if request.method == 'POST' and 'agencyid' in request.form and 'agencyname' in request.form and 'agencycountry' in request.form and 'agencyyear' in request.form:
        agency_id = request.form['agencyid']
        agency_name = request.form['agencyname']
        country = request.form['agencycountry']
        establishment_year = request.form['agencyyear']

        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Space_Agencies WHERE agency_id = :1", (agency_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Agency ID already exists. Please choose a different ID.")
        else:
            cursor.execute("INSERT INTO Starborn_Space_Agencies (agency_id, agency_name, country, establishment_year) VALUES (:agencyid, :agency_name, :country, :establishment_year)", 
            {'agency_id': agency_id, 'agency_name': agency_name, 'country': country, 'establishment_year': establishment_year})
            print("Record inserted successfully.")
    
    return render_template('agencies.html')

@app.route('/budget')
def budget():
    if request.method == 'POST' and 'missionid' in request.form and 'amount' in request.form and 'agencyid' in request.form:
        mission_id = request.form['missionid']
        budget_amount = request.form['amount']
        agency_id = request.form['agencyid']
       
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Space_Budgets WHERE Mission_id = :1", (mission_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Mission ID already exists. Please choose a different ID.")
        else:
            # Insert values into Space Exploration Budgets Table
            cursor.execute("INSERT INTO Starborn_Space_Budgets (mission_id, agency_id, budget_amount) VALUES (:mission_id, :agency_id, :budget_amount)", 
            {'mission_id': mission_id, 'agency_id': agency_id, 'budget_amount': budget_amount})
            print("Record inserted successfully.")
    
    return render_template('budget.html')

@app.route('/exoplanets')
def exoplanets():
    if request.method == 'POST' and 'exoplanetid' in request.form and 'exoplanetname' in request.form and 'discoverymethod' in request.form and 'discoveryyear' in request.form and 'distancefromearth' in request.form and 'hoststarid' in request.form:
        exoplanet_id = request.form['exoplanetid']
        exoplanetname = request.form['exoplanetname']
        discoverymethod = request.form['discoverymethod']
        discoveryyear = request.form['discoveryyear']
        distancefromearth = request.form['distancefromearth']
        hoststarid = request.form['hoststarid']
       
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Exoplanets WHERE exoplanet_id = :1", (exoplanet_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Exoplanet ID already exists. Please choose a different ID.")
        else:
            # Insert values into Space Exploration Budgets Table
            cursor.execute("INSERT INTO Starborn_Exoplanets (exoplanet_id,exoplanet_name, discovery_method, discovery_year, distance_from_earth, host_star_id) VALUES (:1, :2, :3, :4, :5, :6)", 
            (exoplanet_id,exoplanetname,discoverymethod,discoveryyear,distancefromearth,hoststarid))
            print("Record inserted successfully.")
    
    return render_template('exoplanets.html')

@app.route('/planets')
def planets():
    if request.method == 'POST' and 'planetid' in request.form and 'planetname' in request.form and 'discoverymethod' in request.form and 'discoveryyear' in request.form and 'distancefromearth' in request.form and 'hoststarid' in request.form:
        planet_id = request.form['planetid']
        planetname = request.form['planetname']
        diameter = request.form['diameter']
        noofmoons = request.form['noofmoons']
        distancefromhost = request.form['distancefromhost']
        hoststarid = request.form['hoststarid']
       
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Planets WHERE planet_id = :1", (planet_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Planet ID already exists. Please choose a different ID.")
        else:
            # Insert values into Space Exploration Budgets Table
            cursor.execute("INSERT INTO Starborn_Exoplanets (planet_id,planet_name,diameter,no_of_moons,distance_from_host, host_star_id) VALUES (:1, :2, :3, :4, :5, :6)", 
            (planet_id,planetname,diameter,noofmoons,distancefromhost, hoststarid))
            print("Record inserted successfully.")
    
    return render_template('planets.html')

@app.route('/spacecrafts')
def spacecrafts():
    if request.method == 'POST' and 'spacecraftid' in request.form and 'spacecraftname' in request.form and 'inauguraldate' in request.form and 'manufacturer' in request.form:
        spacecraft_id = request.form['spacecraftid']
        spacecraft_name = request.form['spacecraftname']
        inaugural_date = request.form['inauguraldate']
        manufacturer = request.form['manufacturer']
        
       
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Spacecrafts WHERE spacecraft_id = :1", (spacecraft_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Spacecraft ID already exists. Please choose a different ID.")
        else:
            # Insert values into Space Exploration Budgets Table
            cursor.execute("INSERT INTO Spacecrafts (spacecraft_id, spacecraft_name, inaugural_date, manufacturer) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)", 
            (spacecraft_id, spacecraft_name, inaugural_date, manufacturer))
            print("Record inserted successfully.")
    
    return render_template('spacecrafts.html')

@app.route('/stars', methods=['GET', 'POST'])
def stars():
    if request.method == 'POST' and 'starid' in request.form and 'starname' in request.form:
        star_id = request.form['starid']
        star_name = request.form['starname']
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Stars WHERE star_id = :1", (star_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Star ID already exists. Please choose a different ID.")
        else:
            cursor.execute("INSERT INTO Starborn_Stars (star_id, star_name) VALUES (:1, :2)", (star_id, star_name))
            print("Record inserted successfully.")
    
    return render_template('stars.html')

@app.route('/astronauts')
def astronauts():
    return render_template('astronauts.html')

@app.route('/launchsites')
def launchsites():
    return render_template('launchsites.html')

@app.route('/missions')
def misions():
    return render_template('missions.html')

@app.route('/spaceevents')
def spaceevents():
    return render_template('spaceevents.html')


if __name__ == "__main__":
    app.run(debug=True)
