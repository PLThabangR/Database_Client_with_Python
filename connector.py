import mysql.connector as connector

try:
    connection=connector.connect(
        user="root",
        password=""
       )

except connector.Error as er:
    print("Error code:", er.errno)
    print("Error message:", er.msg)

#Create a cursor object
cursor = connection.cursor()

cursor.execute("CREATE DATABASE little_lemon")

cursor.execute("show databases")

for database in cursor:
    print(database)

#Use this database
cursor.execute("use little_lemon")

#check which database is connected
connection.database


#Create menu items table
create_menuitem_table = """CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

cursor.execute(create_menuitem_table)

#Show tables
cursor.execute("show tables")
for tables in cursor:
    print(tables)

###############################create new table
create_menu = """CREATE TABLE Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID,ItemID)
);"""

cursor.execute(create_menu)

#Show tables
cursor.execute("show tables")
for tables in cursor:
    print(tables)
#####################Creating a booking table
Create_booking_table = """CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""

cursor.execute(Create_booking_table)


create_orders_table = """CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""

cursor.execute(create_orders_table)

#Show tables
cursor.execute("show tables")
for tables in cursor:
    print(tables)