# Task 1

# The SQL query is:
join_query="""SELECT 
MenuItems.Name AS Item_Name, 
MenuItems.Type AS Item_Type, 
Menus.Cuisine AS Cuisine, 
MenuItems.Price AS Price 
FROM MenuItems 
INNER JOIN Menus ON MenuItems.ItemID=Menus.ItemID;"""

# Execute query
cursor.execute(join_query)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)   

####################################################
# Task 2
# Good to specify column from the table
# Try left, right, inner

# The SQL query is:
join_query="""SELECT 
MenuItems.Name AS Item_Name, 
MenuItems.Type AS Item_Type, 
Menus.Cuisine AS Cuisine, 
MenuItems.Price AS Price 
FROM MenuItems 
LEFT JOIN Menus ON MenuItems.ItemID=Menus.ItemID
WHERE Cuisine IS NULL;"""

# Execute query
cursor.execute(join_query)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)    

##############################################
##########################################
# Task 3

# The SQL query is:
join_query="""SELECT 
Bookings.BookingID,
Bookings.TableNo,
Bookings.GuestFirstName,
Bookings.EmployeeID AS ServerID,
Orders.BillAmount
FROM Bookings
LEFT JOIN Orders ON Bookings.BookingID = Orders.BookingID;
"""

# Execute query
cursor.execute(join_query)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)    


# Let's close the cursor and the connection
if connection.is_connected():
    cursor.close()
    print("The cursor is closed.")
    connection.close()
    print("MySQL connection is closed.")
else:
    print("Connection is already closed")