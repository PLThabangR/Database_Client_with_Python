stored_procedure_query="""
CREATE PROCEDURE PeakHours()

BEGIN

SELECT count(bookingID) as nobooking, hour(BookingSlot) as hour
FROM Bookings
group by hour
order by nobooking desc;

END

"""

# Execute the query
cursor.execute(stored_procedure_query)

#********************************************#

# Call the stored procedure with its name
cursor.callproc("PeakHours")

# Retrieve recrods in "dataset"
results = next( cursor.stored_results() )
dataset = results.fetchall()

# Retrieve column names using list comprehension in a 'for' loop 
for column_id in cursor.stored_results():
    columns = [ column[0] for column in column_id.description ]

# step 6 Print column names
print(columns)

# Print data 
for data in dataset:
    print(data)