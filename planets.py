import cx_Oracle

# Function to get user input for planets
def get_planet_data():
    planet_name = input("Enter planet name: ")
    diameter = input("Enter diameter (in kilometers): ")
    distance_from_sun = input("Enter distance from sun (in AU): ")
    return (planet_name, diameter, distance_from_sun)

# Connect to the database
dsn = cx_Oracle.makedsn("localhost", "1521", "ORCL")
conn = cx_Oracle.connect(user="system", password="oracle_1234")
c = conn.cursor()

# Insert values into the Planets table
print("Enter Planet Details:")
planet_data = get_planet_data()
c.execute('''INSERT INTO Planets (planet_name, diameter, distance_from_sun)
             VALUES (:1, :2, :3)''', planet_data)

# Commit changes and close connection
conn.commit()
conn.close()
