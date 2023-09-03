################################################################################
# Airlines reservation project (Database structure creation)                   #
# By Pranesh Umasankar                                                         #
################################################################################

import pymysql

# database connection
conn=pymysql.connect(host='localhost',user='root',password='PranesH')

if not conn:
    print('''Database connection failure, Possible errors are\n
            1 - MySQL server is not running\n
            2 - Database airlines does not exist''')
    exit(1)

# create cursor
cursor = conn.cursor()

# drop airlines database if exists
cursor.execute('drop database if exists airlines;')

# create airlines database if not exists
cursor.execute('create database if not exists airlines;')

# activate airlines database
cursor.execute('use airlines;')

# create admin table
sql_query = """create table admin 
                (
                    admin_id int not null primary key,
                    user_name varchar(50) not null unique,
                    password varchar(50) not null,
                    logged_status char(1) not null default 'N'
                );"""

cursor.execute(sql_query)
print('admin table created successfully')

# create customer table
sql_query = """create table customer 
                (
                    customer_id bigint unsigned not null primary key auto_increment,
                    first_name varchar(50) not null,
                    last_name varchar(50) not null,
                    mobile_no bigint unsigned not null unique,
                    password varchar(16) not null,
                    gender char(1) not null,
                    dob date not null,
                    address1 varchar(50) not null,
                    address2 varchar(50) null,
                    pin mediumint unsigned not null,
                    logged_status char(1) not null default 'N'
                )auto_increment = 1001;"""

cursor.execute(sql_query)
print('customer table created successfully')
    
# create flight table
sql_query = """create table flight 
                (
                    flight_id int unsigned not null primary key auto_increment,
                    flight_number varchar(10) not null unique,
                    flight_name varchar(50) not null,
                    origin varchar(50) not null,
                    destination varchar(50) not null,
                    fare decimal(10,2) not null,
                    total_seats smallint unsigned not null,
                    available_seats smallint unsigned not null,
                    is_active char(1) not null default 'Y'
                )auto_increment = 1001;"""

cursor.execute(sql_query)
print('flight table created successfully')
    
# create booking table
sql_query = """create table booking 
                (
                    booking_id int not null primary key auto_increment,
                    booked_by bigint unsigned not null,
                    flight_number varchar(10) not null,
                    booking_date date not null,
                    travel_date date not null,
                    id_proof varchar(20) not null,
                    total_passenger tinyint unsigned not null,
                    passenger_name_1 varchar(50) not null,
                    passenger_age_1 tinyint unsigned not null,
                    passenger_name_2 varchar(50) default null,
                    passenger_age_2 tinyint unsigned default null,
                    passenger_name_3 varchar(50) default null,
                    passenger_age_3 tinyint unsigned default null,
                    total_fare decimal(10,2) not null,
                    booking_status varchar(10) not null,
                    foreign key fk_mobile (booked_by) 
                    references customer (mobile_no) on delete cascade on update cascade,
                    foreign key fk_flight_number (flight_number) 
                    references flight (flight_number) on delete cascade on update cascade
                )auto_increment = 1001;"""


cursor.execute(sql_query)
print('booking table created successfully')

sql_query = "insert into admin (admin_id, user_name, password) values(%s, %s, %s);"
    
values = [
            (1,'admin','admin123'),
            (2,'sysadmin','sysadmin123')
        ]

row_affected = 0
row_affected = cursor.executemany(sql_query, values)

# commit the changes
conn.commit()

if row_affected >= 1:
    print(row_affected,'rows inserted')
    print(cursor.rowcount, "rows inserted")
else:
    print('Error in inserting admin record')

# close cursor
cursor.close()

# close connection
conn.close()
