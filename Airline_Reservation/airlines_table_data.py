################################################################################
# Airlines reservation project (Database structure creation)                   #
# By Pranesh Umasankar                                                         #
################################################################################

import pymysql

# database connection
conn=pymysql.connect(host='localhost',user='root',password='PranesH',database='airlines')

if not conn:
    print('''Database connection failure, Possible errors are\n
            1 - MySQL server is not running\n
            2 - Database airlines does not exist''')
    exit(1)

# create cursor
cursor = conn.cursor()

sql_query = "insert into customer (first_name,last_name,mobile_no,password,gender,dob,address1,address2,pin) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
values = [
            ('Gopal','Krishnan',9999988888,'cust111','M','1970-1-1','13, 7th main, BTM 2nd stage','Bengaluru',560076),
            ('Manoj','Singh',8888877777,'cust222','M','1980-1-1','29, 17th main, BSK 2nd stage','Delhi',110076),
            ('Guru','Sekar',6666688888,'cust333','M','1985-10-10','145, 5th main, BTM 2nd stage','Mumbai',400046),
            ('Paneer','Kumar',8888899999,'cust444','M','1990-10-20','176, 6th main, T.Nagar 2nd Avenue','Chennai',600026),
            ('Hari','Shankar',7777788888,'cust555','M','2000-10-20','200, 9th main, BTM 2nd stage','Kolkata',310076),
            ('Heera','Singh',7777722222,'cust666','F','2000-10-30','150, 9th main, Ram Nagar','Kolkata',310076),
            ('Meera','Gupta',7777733333,'cust777','F','2000-10-30','150, 9th main, T Nagar','Chennai',600076)
        ]

row_affected = 0
row_affected = cursor.executemany(sql_query, values)

# commit the changes
conn.commit()

if row_affected >= 1:
    print(cursor.rowcount, "rows inserted into customer table")
else:
    print('Error in inserting customer table record')

# flight data
sql_query = "insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats) values(%s, %s, %s, %s, %s, %s, %s)"
    
values = [
            ('G8285','GO FIRST','Bengaluru','Delhi',6000,300,300),
            ('G8195','GO FIRST','Bengaluru','Delhi',5000,700,700),
            ('G8320','GO FIRST','Bengaluru','Delhi',8000,250,250),
            ('G8345','GO FIRST','Bengaluru','Delhi',3000,1000,1000),
            ('E6813','IndiGo','Bengaluru','Delhi',6500,500,500),
            ('E5356','IndiGo','Bengaluru','Delhi',5500,700,700),
            ('E2402','IndiGo','Bengaluru','Delhi',8500,250,250),
            ('E5306','IndiGo','Bengaluru','Delhi',3500,1000,1000),
            ('E6239','IndiGo','Chennai','Delhi',5500,600,600),
            ('E2053','IndiGo','Chennai','Delhi',4500,800,800),
            ('UK864','Vistara','Chennai','Delhi',6500,450,450),
            ('UK910','Vistara','Chennai','Delhi',7500,800,800),
            ('UK994','Vistara','Chennai','Mumbai',5500,450,450),
            ('UK850','Vistara','Chennai','Mumbai',6500,800,800),
            ('UK836','Vistara','Chennai','Kolkata',7000,450,450),
            ('UK832','Vistara','Chennai','Cochin',3500,1000,1000),
            ('S8134','SpiceJet','Bengaluru','Mumbai',5500,450,450),
            ('S5353','SpiceJet','Bengaluru','Mumbai',6500,800,800),
            ('S2909','SpiceJet','Bengaluru','Kolkata',7000,450,450),
            ('S8641','SpiceJet','Bengaluru','Cochin',3500,800,800),
            ('S8412','SpiceJet','Bengaluru','Chennai',3500,800,800),
            ('AI503','Air India','Mumbai','Bengaluru',5500,450,450),
            ('AI511','Air India','Mumbai','Bengaluru',4500,800,800),
            ('AI808','Air India','Mumbai','Bengaluru',5000,450,450),
            ('AI610','Air India','Bengaluru','Chennai',5000,450,450),
            ('E6269','IndiGo','Bengaluru','Chennai',4000,450,450),
            ('E6017','IndiGo','Bengaluru','Chennai',3500,450,450),
            ('I5145','AirAsia India','Bengaluru','Mumbai',5000,450,450),
            ('I5246','AirAsia India','Bengaluru','Mumbai',5500,450,450),
            ('I5611','AirAsia India','Bengaluru','Mumbai',5500,450,450),
            ('Q1307','Akasa Air','Bengaluru','Kolkata',5000,450,450),
            ('Q1321','Akasa Air','Bengaluru','Kolkata',4500,750,750),
            ('Q1327','Akasa Air','Kolkata','Bengaluru',5000,450,450),
            ('Q1313','Akasa Air','Chennai','Bengaluru',5500,450,450),
            ('Q1319','Akasa Air','Cochin','Chennai',5000,450,450),
            ('E5307','IndiGo','Mumbai','Chennai',3000,450,450),
            ('E5303','IndiGo','Mumbai','Chennai',3500,750,750),
            ('S6113','SpiceJet','Mumbai','Delhi',4000,550,550),
            ('S2514','SpiceJet','Mumbai','Kolkata',3500,650,650),
            ('UK920','Vistara','Mumbai','Delhi',4000,550,550),
            ('E2056','IndiGo','Mumbai','Delhi',4500,750,750),
            ('E2111','IndiGo','Mumbai','Delhi',4000,350,350),
            ('E2083','IndiGo','Mumbai','Delhi',4500,750,750),
            ('G8319','GO FIRST','Mumbai','Delhi',4000,650,650),
            ('G8327','GO FIRST','Mumbai','Delhi',4500,550,550),
            ('G8329','GO FIRST','Mumbai','Delhi',4700,550,550),
            ('S8263','SpiceJet','Delhi','Kolkata',4000,450,450),
            ('S8253','SpiceJet','Delhi','Kolkata',7500,650,650),
            ('E5353','IndiGo','Delhi','Kolkata',8000,550,550),
            ('G8101','GO FIRST','Delhi','Kolkata',6500,750,750),
            ('E6903','IndiGo','Delhi','Chennai',4000,450,450),
            ('G8336','GO FIRST','Delhi','Chennai',7500,650,650),
            ('G8354','GO FIRST','Delhi','Chennai',8000,550,550),
            ('I5821','AirAsia India','Chennai','Bengaluru',4000,450,450),
            ('I5612','AirAsia India','Chennai','Bengaluru',7500,650,650),
            ('I5146','AirAsia India','Chennai','Bengaluru',8000,550,550),
            ('Q1316','Akasa Air','Chennai','Bengaluru',6500,750,750),
            ('Q1322','Akasa Air','Chennai','Bengaluru',4000,450,450),
            ('AI785','Air India','Kolkata','Chennai',7500,450,450),
            ('E6214','IndiGo','Kolkata','Chennai',8500,450,450),
            ('E7561','IndiGo','Kolkata','Chennai',8000,450,450),
            ('AI800','AirAsia India','Kolkata','Chennai',8000,450,450),
            ('G8227','GO FIRST','Kolkata','Delhi',5500,650,650),
            ('G8102','GO FIRST','Kolkata','Delhi',6500,750,750),
            ('E6917','IndiGo','Kolkata','Delhi',6000,500,500),
            ('S8264','SpiceJet','Kolkata','Delhi',6500,450,450),
            ('S2421','SpiceJet','Kolkata','Mumbai',8500,650,650),
            ('S4891','SpiceJet','Kolkata','Mumbai',9500,650,650),
            ('E6717','IndiGo','Kolkata','Mumbai',9000,650,650),
            ('E6215','IndiGo','Kolkata','Mumbai',9500,650,650),
            ('G8514','GO FIRST','Kolkata','Mumbai',7000,650,650),
            ('G8512','GO FIRST','Kolkata','Mumbai',7500,650,650)
        ]

row_affected = 0
row_affected = cursor.executemany(sql_query, values)

# commit the changes
conn.commit()

if row_affected >= 1:
    print(cursor.rowcount, "rows inserted into flight table")
else:
    print('Error in inserting flight table record')

# close cursor
cursor.close()

# close connection
conn.close()
