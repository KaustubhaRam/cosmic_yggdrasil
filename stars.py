import cx_Oracle

# Connect to the Oracle database
conn = cx_Oracle.connect('username/password@hostname:port/service_name')

# Create a cursor object
cur = conn.cursor()

# Create a table called 'stars' with attributes 'star_id' and 'star_name'
cur.execute('CREATE TABLE stars (star_id NUMBER PRIMARY KEY, star_name VARCHAR2(50))')

# Insert data into the 'stars' table
star_id = int(input("Enter star ID: "))
star_name = input("Enter star name: ")
cur.execute("INSERT INTO stars (star_id, star_name) VALUES (:1, :2)", (star_id, star_name))

# Delete data from the 'stars' table
delete_id = int(input("Enter star ID to delete: "))
cur.execute("DELETE FROM stars WHERE star_id = :1", (delete_id,))

# Update data in the 'stars' table
update_id = int(input("Enter star ID to update: "))
new_name = input("Enter new star name: ")
cur.execute("UPDATE stars SET star_name = :1 WHERE star_id = :2", (new_name, update_id))

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()