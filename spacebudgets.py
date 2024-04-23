import cx_Oracle

# Connect to the database
conn = cx_Oracle.connect('system/oracle_1234@localhost:1521/xe')
c = conn.cursor()

# Prompt user for input
agency_id = input("Enter agency ID: ")
budget_amount = input("Enter budget amount: ")

# Insert values into Space Exploration Budgets Table
c.execute("INSERT INTO Space_Exploration_Budgets (agency_id, budget_amount) VALUES (:agency_id, :budget_amount)", 
          {'agency_id': agency_id, 'budget_amount': budget_amount})

# Commit changes and close connection
conn.commit()
conn.close()