import datetime as dt
topSpender = """create procedure()
begin
select bookingID,guestFullName,billAmount from 
Booking as b inner join Order as o on b.TableNo = o.TableNo 
end
"""
cursor.execute("DROP PROCEDURE IF EXISTS TopSpender;")

# Call the stored procedure with its name
cursor.callproc("TopSpender")

# Retrieve recrods in "dataset"
results = next(cursor.stored_results())
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop 
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)

###############################################################
    ###############################################################################
##############################################################
# Stored procedure name >> NoArrival
# Our stored procedure query is
stored_procedure_query="""
CREATE PROCEDURE NoArrival()

BEGIN

SELECT bookings.BookingID, 
Orders.BillAmount 
FROM Bookings
LEFT JOIN
Orders ON Bookings.BookingID=Orders.BookingID
WHERE BillAmount IS NULL;

END

"""

# Execute the query 
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("NoArrival")

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

###########################################################################
    ########################################################################################
##########################################################
# Task 3
# Stored procedure name >> OrderStatus
# Our stored procedure query is
stored_procedure_query="""
CREATE PROCEDURE OrderStatus()

BEGIN

SELECT bookingID, 
CASE
WHEN employeeID IN (1,2,3) THEN "Order Served" 
WHEN employeeID IN (4,5) THEN "Preparing Order" 
ELSE "In Queue" 
END AS Status
FROM Bookings;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("OrderStatus")

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