import cx_Oracle

# Function to get user input for missions
def get_mission_data():
    mission_name = input("Enter mission name: ")
    launch_date = input("Enter launch date (YYYY-MM-DD): ")
    destination = input("Enter destination: ")
    duration = input("Enter duration (in years): ")
    mission_status = input("Enter mission status: ")
    spacecraft_id = input("Enter spacecraft ID: ")
    return (mission_name, launch_date, destination, duration, mission_status, spacecraft_id)

# Connect to the database
dsn = cx_Oracle.makedsn("localhost", "1521", "ORCL")
conn = cx_Oracle.connect(user="system", password="oracle_1234")
c = conn.cursor()

# Insert values into the Missions table
mission_data = get_mission_data()
c.execute('''INSERT INTO Missions (mission_name, launch_date, destination, duration, mission_status, spacecraft_id)
             VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4, :5, :6)''', mission_data)

# Commit changes and close connection
conn.commit()
conn.close()
