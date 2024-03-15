stored_procedure_status="""
CREATE PROCEDURE GuestStatus()

BEGIN

SELECT concat(b.GuestFirstName," ",b.GuestLastName) as GuestFullName,
CASE
WHEN e.role IN ("Manager","Assistant Manager") THEN "Ready to pay" 
WHEN e.role = "Head Chef" THEN "Ready to serve"
WHEN e.role ="Assistant Chef" THEN "Preparing Order"
WHEN e.role = "Head Waiter" THEN "Order Served"
ELSE "In Queue" 
END AS Status
FROM Employees as e left join Bookings as b on e.EmployeeID = b.EmployeeID ;

END

"""

# Execute the query
cursor.execute("DROP PROCEDURE IF EXISTS stored_procedure_status")

#********************************************#

# Call the stored procedure with its name
cursor.callproc("GuestStatus")

# Retrieve recrods in "dataset"
results = next( cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop 
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)




# Let's close the cursor and the connection
if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")