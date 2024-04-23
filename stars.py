import cx_Oracle

# Connect to the Oracle database
conn = cx_Oracle.connect('system/oracle_1234@localhost:1521/xe')

# Create a cursor object
cur = conn.cursor()


# Delete data from the 'stars' table
delete_id = int(input("Enter star ID to delete: "))
cur.execute("DELETE FROM stars WHERE star_id = :1", (delete_id,))
if cur.rowcount == 0:
    print("Error: Star ID not found. No records deleted.")
else:
    print("Record deleted successfully.")

# Update data in the 'stars' table
update_id = int(input("Enter star ID to update: "))
new_name = input("Enter new star name: ")
cur.execute("UPDATE stars SET star_name = :1 WHERE star_id = :2", (new_name, update_id))
if cur.rowcount == 0:
    print("Error: Star ID not found. No records updated.")
else:
    print("Record updated successfully.")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()