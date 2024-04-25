import cx_Oracle

# Establish a connection to the Oracle database
try:
    # Connect using your credentials and Oracle SID
    con = cx_Oracle.connect('system/mysql@localhost:1521/xe')
    print("Connected to Oracle Database", con.version)
    cursor = con.cursor()

    # Drop existing tables (optional, be careful with this in a production environment)
    drop_statements = [
        "DROP TABLE Starborn_Space_Budgets",
        "DROP TABLE Starborn_Space_Events",
        "DROP TABLE Starborn_Launch_Sites",
        "DROP TABLE Starborn_Exoplanets",
        "DROP TABLE Starborn_Planets",
        "DROP TABLE Starborn_Astronauts",
        "DROP TABLE Starborn_Missions",
        "DROP TABLE Starborn_Spacecrafts",
        "DROP TABLE Starborn_Stars",
        "DROP TABLE Starborn_Space_Agencies",
        "DROP TABLE Starborn_Login",
    ]
    for statement in drop_statements:
        try:
            cursor.execute(statement)
        except cx_Oracle.DatabaseError as e:
            print("Ignoring error while dropping tables:", e)

    # Create table commands
    cursor.execute("""
        CREATE TABLE Starborn_Stars (
            star_id NUMBER PRIMARY KEY,
            star_name VARCHAR2(255) NOT NULL
        )""")
    cursor.execute("""
        CREATE TABLE Starborn_Spacecrafts (
            spacecraft_id NUMBER PRIMARY KEY,
            spacecraft_name VARCHAR2(255) NOT NULL,
            manufacturer VARCHAR2(255) NOT NULL,
            inaugural_date DATE
        )""")
    
    cursor.execute("""
        CREATE TABLE Starborn_Astronauts (
            astronaut_id NUMBER PRIMARY KEY,
            astronaut_name VARCHAR2(255) NOT NULL,
            nationality VARCHAR2(255) NOT NULL,
            birth_date DATE
        )""")
    cursor.execute("""
        CREATE TABLE Starborn_Planets (
            planet_id NUMBER PRIMARY KEY,
            planet_name VARCHAR2(255) NOT NULL,
            diameter NUMBER,
            distance_from_host NUMBER,
            number_of_moons NUMBER,
            host_star_id NUMBER,
            CONSTRAINT fk_stars FOREIGN KEY (host_star_id) REFERENCES Starborn_Stars(star_id)
        )""")
    cursor.execute("""
        CREATE TABLE Starborn_Exoplanets (
            exoplanet_id NUMBER PRIMARY KEY,
            exoplanet_name VARCHAR2(255) NOT NULL,
            discovery_method VARCHAR2(255),
            discovery_year DATE,
            distance_from_earth NUMBER,
            host_star_id NUMBER
        )""")
    cursor.execute("""
        CREATE TABLE Starborn_Launch_Sites (
            launch_site_id NUMBER PRIMARY KEY,
            launch_site_name VARCHAR2(255) NOT NULL,
            country VARCHAR2(255) NOT NULL,
            latitude NUMBER(9,6),
            longitude NUMBER(9,6)
        )""")
    cursor.execute("""
        CREATE TABLE Starborn_Space_Events (
            event_id NUMBER PRIMARY KEY,
            event_name VARCHAR2(255) NOT NULL,
            event_date DATE,
            description VARCHAR2(1000)
        )""")
    cursor.execute("""
        CREATE TABLE Starborn_Space_Agencies (
            agency_id NUMBER PRIMARY KEY,
            agency_name VARCHAR2(255) NOT NULL,
            country VARCHAR2(255) NOT NULL,
            establishment_year DATE
        )""")
    cursor.execute("""
        CREATE TABLE Starborn_Space_Budgets (
            budget_id NUMBER PRIMARY KEY,
            agency_id NUMBER,
            budget_amount NUMBER,
            FOREIGN KEY (agency_id) REFERENCES Starborn_Space_Agencies(agency_id)
        )""")
    
    cursor.execute("""
        CREATE TABLE Starborn_Missions (
            mission_id NUMBER PRIMARY KEY,
            mission_name VARCHAR2(255) NOT NULL,
            launch_date DATE,
            destination VARCHAR2(255),
            duration NUMBER,
            mission_status VARCHAR2(255),
            budget_id NUMBER,
            spacecraft_id NUMBER,
            CONSTRAINT fk_spacecraft FOREIGN KEY (spacecraft_id) REFERENCES Starborn_Spacecrafts(spacecraft_id),
            CONSTRAINT fk_budget FOREIGN KEY (budget_id) REFERENCES Starborn_Space_Budgets(budget_id)
        )""")
    
    cursor.execute("""
        CREATE TABLE Starborn_Login (
            username VARCHAR2(255) PRIMARY KEY,
            password VARCHAR2(255)
        )""")
    
    cursor.execute("""
        INSERT INTO Starborn_Login VALUES(
            'user','pwd'
        )""")

    # Commit the changes to the database
    con.commit()
    print("All tables created successfully.")

except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("Oracle Error encountered:", error.code)
    print(error.message)

finally:
    # Ensure the cursor and connection are closed properly
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Oracle connection is closed")
