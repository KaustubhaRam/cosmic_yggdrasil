import cx_Oracle

# Function to get user input for launch sites
def get_launch_site_data():
    launch_site_name = input("Enter launch site name: ")
    country = input("Enter country: ")
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    return (launch_site_name, country, latitude, longitude)

# Connect to the database
dsn = cx_Oracle.makedsn("localhost", "1521", "ORCL")
conn = cx_Oracle.connect(user="system", password="oracle_1234")
c = conn.cursor()

# Insert values into the Launch Sites table
print("Enter Launch Site Details:")
launch_site_data = get_launch_site_data()
c.execute('''INSERT INTO Launch_Sites (launch_site_name, country, latitude, longitude)
             VALUES (:1, :2, :3, :4)''', launch_site_data)

# Commit changes and close connection
conn.commit()
conn.close()
