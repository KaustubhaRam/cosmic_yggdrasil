import cx_Oracle

# Connect to the database
conn = cx_Oracle.connect('system/oracle_1234@localhost:1521/xe')
c = conn.cursor()

# Prompt user for input
event_name = input("Enter event name: ")
event_date = input("Enter event date (YYYY-MM-DD): ")
description = input("Enter event description: ")

# Insert values into Space Events Table
c.execute("INSERT INTO Space_Events (event_name, event_date, description) VALUES (:event_name, :event_date, :description)", 
          {'event_name': event_name, 'event_date': event_date, 'description': description})

# Commit changes and close connection
conn.commit()
conn.close()