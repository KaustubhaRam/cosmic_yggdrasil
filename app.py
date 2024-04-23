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

@app.route('/agencies', methods=['GET', 'POST'])
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

@app.route('/budget', methods=['GET', 'POST'])
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

@app.route('/exoplanets', methods=['GET', 'POST'])
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

@app.route('/planets', methods=['GET', 'POST'])
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
    
    return render_template('planets.html', methods=['GET', 'POST'])

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
    
    return render_template('spacecrafts.html', methods=['GET', 'POST'])

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

@app.route('/astronauts', methods=['GET', 'POST'])
def astronauts():
    if request.method == 'POST' and 'astronautid' in request.form and 'astronautname' in request.form and 'birthdate' in request.form and 'nationality' in request.form:
        astronaut_id = request.form['astronautid']
        astronaut_name = request.form['astronautname']
        birth_date = request.form['birthdate']
        nationality = request.form['nationality']
        
       
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Astronauts WHERE astronaut_id = :1", (astronaut_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Astronaut ID already exists. Please choose a different ID.")
        else:
            # Insert values into Space Exploration Budgets Table
            cursor.execute("INSERT INTO Starborn_Astronauts (astronaut_id, astronaut_name, birth_date, nationality) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)", 
            (astronaut_id, astronaut_name, birth_date, nationality))
            print("Record inserted successfully.")
    
    return render_template('astronauts.html', methods=['GET', 'POST'])

@app.route('/launchsites', methods=['GET', 'POST'])
def launchsites():
    if request.method == 'POST' and 'launchsiteid' in request.form and 'launchsitename' in request.form and 'country' in request.form and 'latitude' in request.form and 'longitude' in request.form:
        launch_site_id = request.form['launchsiteid']
        launch_site_name = request.form['launchsitename']
        country = request.form['country']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        
       
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Launch_Sites WHERE launch_site_id = :1", (launch_site_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Launch Site ID already exists. Please choose a different ID.")
        else:
            # Insert values into Space Exploration Budgets Table
            cursor.execute("INSERT INTO Starborn_Launch_Sites (launch_site_id, launch_site_name, country, latitude, longitude) VALUES (:1, :2, :3, :4, :5)", 
            (launch_site_id, launch_site_name, country, latitude, longitude))
            print("Record inserted successfully.")
    
    return render_template('launchsites.html')

@app.route('/missions', methods=['GET', 'POST'])
def misions():
    if request.method == 'POST' and 'missionid' in request.form and 'missionname' in request.form and 'launchdate' in request.form and 'destination' in request.form and 'duration' in request.form and 'missionstatus' in request.form and 'spacecraftid' in request.form:
        mission_id = request.form['missionid']
        mission_name = request.form['missionname']
        launch_date = request.form['launchdate']
        destination = request.form['destination']
        duration = request.form['duration']
        mission_status = request.form['missionstatus']
       
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Missions WHERE mission_id = :1", (mission_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Mission ID already exists. Please choose a different ID.")
        else:
            # Insert values into Space Exploration Budgets Table
            cursor.execute("INSERT INTO Starborn_Missions (mission_id, mission_name, launch_date, destination, duration, mission_status, spacecraft_id) VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5, :6, :7)", 
            (mission_id, mission_name, launch_date, destination, duration, mission_status))
            print("Record inserted successfully.")
    
    return render_template('missions.html')

@app.route('/spaceevents', methods=['GET', 'POST'])
def spaceevents():
    if request.method == 'POST' and 'eventid' in request.form and 'eventname' in request.form and 'eventdate' in request.form and 'description' in request.form:
        event_id = request.form['eventid']
        event_name = request.form['eventname']
        event_date = request.form['eventdate']
        description = request.form['description']
        
       
        # Check if star_id already exists
        cursor.execute("SELECT COUNT(*) FROM Starborn_Space_Events WHERE event_id = :1", (event_id,))
        result = cursor.fetchone()
        if result[0] > 0:
            print("Error: Event ID already exists. Please choose a different ID.")
        else:
            # Insert values into Space Exploration Budgets Table
            cursor.execute("INSERT INTO Starborn_Space_Events (event_id, event_name, event_date, description) VALUES (:event_id, :event_name, :event_date, :description)", 
            {'event_id': event_id, 'event_name': event_name, 'event_date': event_date, 'description': description})
            print("Record inserted successfully.")
    
    return render_template('spaceevents.html')


if __name__ == "__main__":
    app.run(debug=True)
