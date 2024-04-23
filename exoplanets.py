import cx_Oracle

# Function to get user input for exoplanets
def get_exoplanet_data():
    exoplanet_name = input("Enter exoplanet name: ")
    discovery_method = input("Enter discovery method: ")
    discovery_year = input("Enter discovery year: ")
    distance_from_earth = input("Enter distance from Earth (in light years): ")
    host_star_name = input("Enter host star name: ")
    return (exoplanet_name, discovery_method, discovery_year, distance_from_earth, host_star_name)

# Connect to the database
dsn = cx_Oracle.makedsn("localhost", "1521", "ORCL")
conn = cx_Oracle.connect(user="system", password="oracle_1234")
c = conn.cursor()

# Insert values into the Exoplanets table
print("Enter Exoplanet Details:")
exoplanet_data = get_exoplanet_data()
c.execute('''INSERT INTO Exoplanets (exoplanet_name, discovery_method, discovery_year, distance_from_earth, host_star_name)
             VALUES (:1, :2, :3, :4, :5)''', exoplanet_data)

# Commit changes and close connection
conn.commit()
conn.close()
