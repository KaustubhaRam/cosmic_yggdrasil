# importing module
import cx_Oracle

# Create a table in Oracle database
try:

    con = cx_Oracle.connect('system/oracle_1234@localhost:1521/xe')
    print(con.version)

    # Now execute the sqlquery
    cursor = con.cursor()
    

    sql_create  = """create table planets (Name varchar(20), planetid integer)"""
      
    

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()