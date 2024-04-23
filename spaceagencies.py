import cx_Oracle

# Connect to the database
conn = cx_Oracle.connect('system/oracle_1234@localhost:1521/xe')
c = conn.cursor()

# Prompt user for input
agency_name = input("Enter agency name: ")
country = input("Enter country: ")
establishment_year = input("Enter establishment year: ")

# Insert values into Space Agencies Table
c.execute("INSERT INTO Space_Agencies (agency_name, country, establishment_year) VALUES (:agency_name, :country, :establishment_year)", 
          {'agency_name': agency_name, 'country': country, 'establishment_year': establishment_year})

# Commit changes and close connection
conn.commit()
conn.close()