import datetime as dt

###########String functions
# Add your code here
guestFullName ="""select count(BookingID), sum(BillAmount), avg(BillAmount) from Orders """
cursor.execute(guestFullName)

results = cursor.fetchall()
print(cursor.column_names)
print("Today's statistics:")
for x in results:
    print("Number of booking",x[0])
    print("Total sales",x[1])
    print("Average sale",x[2])




##############Numeric functions
# The SQL query is:
sql_query="""SELECT 
TableNo AS 'Table number', 
COUNT(TableNo) AS n_booking
FROM Bookings 
GROUP BY TableNo 
ORDER BY n_booking DESC;"""

# Execute query
cursor.execute(sql_query)

# Fetch records 
results = cursor.fetchall()

# Retrieve column names
columns = cursor.column_names

# Print column names
print(columns)

# Print query results
for result in results:
    print(result)


################Aggregate functions
# The SQL query is:
sql_query="""
SELECT 
COUNT(BookingID) AS n_bookings,
SUM(BillAmount) AS Total_sale,
AVG(BillAmount) AS Avg_sale
FROM Orders;"""

# Execute query
cursor.execute(sql_query)

# Fetch records
results=cursor.fetchall()

# Print results
print("Today's statistics:")
for result in results:
    print("Number of bookings:",result[0])
    print("Total sale:",result[1])
    print("Average sale:",result[2])


##################Date function
# Add your code here
guestFullName ="""select BookingID,GuestFirstName ,case 
                         when hour(BookingSlot) in (15,16) then "Late afternoon"
                        when hour(BookingSlot) in(17,18) then "Evening"
                        when hour(BookingSlot) in(19,20) then "Night"
                        end as Arrival_slot 
                        
 from Bookings """
cursor.execute(guestFullName)

results = cursor.fetchall()
print(cursor.column_names)

for x in results:
    print(x)
   


###############Comparison functions
####Greatest,Least


################Control flow function
######Case


