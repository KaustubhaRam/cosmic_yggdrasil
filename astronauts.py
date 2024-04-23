import cx_Oracle

# Function to get user input for astronauts
def get_astronaut_data():
    name = input("Enter astronaut's name: ")
    nationality = input("Enter nationality: ")
    birth_date = input("Enter birth date (YYYY-MM-DD): ")
    return (name, nationality, birth_date)

# Connect to the database
dsn = cx_Oracle.makedsn("localhost", "1521", "ORCL")
conn = cx_Oracle.connect(user="system", password="oracle_1234")
c = conn.cursor()

# Insert values into the Astronauts table
print("Enter Astronaut Details:")
astronaut_data = get_astronaut_data()
c.execute('''INSERT INTO Astronauts (name, nationality, birth_date)
             VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'))''', astronaut_data)

# Commit changes and close connection
conn.commit()
conn.close()
