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