
###This continues from the connector.py
################Insert to booking table
insert_booking = """insert into Bookings(BookingID,TableNo,GuestFirstName,GuestLastName,BookingSlot,EmployeeID) values
(1,12,'Anna','Iversen','19:00:00',1),
(2, 12, 'Joakim', 'Iversen', '19:00:00', 1),
(3, 19, 'Vanessa', 'McCarthy', '15:00:00', 3),
(4, 15, 'Marcos', 'Romero', '17:30:00', 4),
(5, 5, 'Hiroki', 'Yamane', '18:30:00', 2),
(6, 8, 'Diana', 'Pinto', '20:00:00', 5);
   """

cursor.execute(insert_booking)

cursor.execute("Select * from Bookings")
print(cursor.fetchall())

################################################################
###############insert to menutiem table
insert_menuitmes="""
INSERT INTO MenuItems (ItemID, Name, Type, Price)
VALUES
(1,'Olives','Starters',5),
(2,'Flatbread','Starters', 5),
(3, 'Minestrone', 'Starters', 8),
(4, 'Tomato bread','Starters', 8),
(5, 'Falafel', 'Starters', 7),
(6, 'Hummus', 'Starters', 5),
(7, 'Greek salad', 'Main Courses', 15),
(8, 'Bean soup', 'Main Courses', 12),
(9, 'Pizza', 'Main Courses', 15),
(10,'Greek yoghurt','Desserts', 7),
(11, 'Ice cream', 'Desserts', 6),
(12, 'Cheesecake', 'Desserts', 4),
(13, 'Athens White wine', 'Drinks', 25),
(14, 'Corfu Red Wine', 'Drinks', 30),
(15, 'Turkish Coffee', 'Drinks', 10),
(16, 'Turkish Coffee', 'Drinks', 10),
(17, 'Kabasa', 'Main Courses', 17);"""

cursor.execute(insert_menuitmes)

cursor.execute("Select * from MenuItems")
print(cursor.fetchall())

#################################################
insert_menu="""
INSERT INTO Menus (MenuID, ItemID, Cuisine)
VALUES
(1, 1, 'Greek'),
(1, 7, 'Greek'),
(1, 10, 'Greek'),
(1, 13, 'Greek'),
(2, 3, 'Italian'),
(2, 9, 'Italian'),
(2, 12, 'Italian'),
(2, 15, 'Italian'),
(3, 5, 'Turkish'),
(3, 17, 'Turkish'),
(3, 11, 'Turkish'),
(3, 16, 'Turkish');"""

cursor.execute(insert_menu)
cursor.execute("Select * from Menus")
print(cursor.fetchall())

#############################################################
insert_orders="""
INSERT INTO Orders (OrderID, TableNo, MenuID, BookingID, Quantity, BillAmount)
VALUES
(1, 12, 1, 1, 2, 86),
(2, 19, 2, 2, 1, 37),
(3, 15, 2, 3, 1, 37),
(4, 5, 3, 4, 1, 40),
(5, 8, 1, 5, 1, 43);"""
cursor.execute(insert_orders)
cursor.execute("Select * from Orders")
print(cursor.fetchall())

#######################################
all_menus = """SELECT GuestFirstName, GuestLastName, TableNo FROM Bookings"""

cursor.execute(all_menus)
print(cursor.column_names)
print(cursor.fetchall())



cursor.execute("Select * from Orders")
print(cursor.fetchall())
######################Display data using a for loop
select_stmt = """SELECT * FROM Menus;"""

cursor.execute(select_stmt)
results= cursor.fetchall()
print(cursor.column_names)
for x in results:
    print(x)