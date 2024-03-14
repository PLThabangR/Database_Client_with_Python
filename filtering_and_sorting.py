filtering_and_sorting = """ SELECT bookingID,billAmount
FROM Orders  where BillAmount >40 order by billAmount desc """

cursor.execute(filtering_and_sorting)

results = cursor.fetchall()
print(cursor.column_names)
for x in results:
    print(x)



    #######################

# Add your code here
select_stmt = """ SELECT tableNo,GuestFirstName, GuestLastName, EmployeeID
FROM Bookings"""

cursor.execute(select_stmt)

results = cursor.fetchall()
print(cursor.column_names)
for x in results:
    print(x)