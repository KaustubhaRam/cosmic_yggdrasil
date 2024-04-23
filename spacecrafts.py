import cx_Oracle

# Function to get user input for spacecrafts
def get_spacecraft_data():
    spacecraft_name = input("Enter spacecraft name: ")
    manufacturer = input("Enter manufacturer: ")
    inaugural_date = input("Enter inaugural date (YYYY-MM-DD): ")
    return (spacecraft_name, manufacturer, inaugural_date)

# Connect to the database
dsn = cx_Oracle.makedsn("localhost", "1521", "ORCL")
conn = cx_Oracle.connect(user="system", password="oracle_1234")
c = conn.cursor()

# Insert values into the Spacecrafts table
print("Enter Spacecraft Details:")
spacecraft_data = get_spacecraft_data()
c.execute('''INSERT INTO Spacecrafts (spacecraft_name, manufacturer, inaugural_date)
             VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'))''', spacecraft_data)

# Commit changes and close connection
conn.commit()
conn.close()
