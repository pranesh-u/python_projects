drop table if exists booking;
drop table if exists flight;
drop table if exists customer;
drop table if exists admin;

drop database if exists airlines;
create database if not exists airlines;

use airlines;

create table admin 
(
  admin_id int not null primary key,
  user_name varchar(50) not null unique,
  password varchar(50) not null,
  logged_status char(1) not null default 'N'
);

create table customer 
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
)auto_increment = 1001;

-- is_active --> Y or N
create table flight 
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
)auto_increment = 1001;

-- class type is Economy, Business, Premium Economy
-- booking_status booked, cancelled
create table booking 
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
)auto_increment = 1001;

-- insert data to admin table
insert into admin (admin_id, user_name, password) values(1,'admin','admin123');
insert into admin (admin_id, user_name, password) values(2,'sysadmin','sysadmin123');

-- insert data to customer table
insert into customer (first_name,last_name,mobile_no,password,gender,dob,address1,address2,pin) values('Gopal','Krishnan',9999988888,'cust111','M','1970-1-1','13, 7th main, BTM 2nd stage','Bengaluru',560076);
insert into customer (first_name,last_name,mobile_no,password,gender,dob,address1,address2,pin) values('Manoj','Singh',8888877777,'cust222','M','1980-1-1','29, 17th main, BSK 2nd stage','Delhi',110076);
insert into customer (first_name,last_name,mobile_no,password,gender,dob,address1,address2,pin) values('Guru','Sekar',6666688888,'cust333','M','1985-10-10','145, 5th main, BTM 2nd stage','Mumbai',400046);
insert into customer (first_name,last_name,mobile_no,password,gender,dob,address1,address2,pin) values('Paneer','Kumar',8888899999,'cust444','M','1990-10-20','176, 6th main, T.Nagar 2nd Avenue','Chennai',600026);
insert into customer (first_name,last_name,mobile_no,password,gender,dob,address1,address2,pin) values('Hari','Shankar',7777788888,'cust555','M','2000-10-20','200, 9th main, BTM 2nd stage','Kolkata',310076);
insert into customer (first_name,last_name,mobile_no,password,gender,dob,address1,address2,pin) values('Heera','Singh',7777722222,'cust666','F','2000-10-30','150, 9th main, Ram Nagar','Kolkata',310076);
insert into customer (first_name,last_name,mobile_no,password,gender,dob,address1,address2,pin) values('Meera','Gupta',7777733333,'cust777','F','2000-10-30','150, 9th main, T Nagar','Chennai',600076);

-- insert data to flight table
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8285','GO FIRST','Bengaluru','Delhi',6000,300,300);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8195','GO FIRST','Bengaluru','Delhi',5000,700,700);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8320','GO FIRST','Bengaluru','Delhi',8000,250,250);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8345','GO FIRST','Bengaluru','Delhi',3000,1000,1000);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6813','IndiGo','Bengaluru','Delhi',6500,500,500);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E5356','IndiGo','Bengaluru','Delhi',5500,700,700);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E2402','IndiGo','Bengaluru','Delhi',8500,250,250);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E5306','IndiGo','Bengaluru','Delhi',3500,1000,1000);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6239','IndiGo','Chennai','Delhi',5500,600,600);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E2053','IndiGo','Chennai','Delhi',4500,800,800);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('UK864','Vistara','Chennai','Delhi',6500,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('UK910','Vistara','Chennai','Delhi',7500,800,800);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('UK994','Vistara','Chennai','Mumbai',5500,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('UK850','Vistara','Chennai','Mumbai',6500,800,800);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('UK836','Vistara','Chennai','Kolkata',7000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('UK832','Vistara','Chennai','Cochin',3500,1000,1000);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S8134','SpiceJet','Bengaluru','Mumbai',5500,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S5353','SpiceJet','Bengaluru','Mumbai',6500,800,800);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S2909','SpiceJet','Bengaluru','Kolkata',7000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S8641','SpiceJet','Bengaluru','Cochin',3500,800,800);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S8412','SpiceJet','Bengaluru','Chennai',3500,800,800);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('AI503','Air India','Mumbai','Bengaluru',5500,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('AI511','Air India','Mumbai','Bengaluru',4500,800,800);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('AI808','Air India','Mumbai','Bengaluru',5000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('AI610','Air India','Bengaluru','Chennai',5000,450,450);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6269','IndiGo','Bengaluru','Chennai',4000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6017','IndiGo','Bengaluru','Chennai',3500,450,450);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('I5145','AirAsia India','Bengaluru','Mumbai',5000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('I5246','AirAsia India','Bengaluru','Mumbai',5500,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('I5611','AirAsia India','Bengaluru','Mumbai',5500,450,450);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('Q1307','Akasa Air','Bengaluru','Kolkata',5000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('Q1321','Akasa Air','Bengaluru','Kolkata',4500,750,750);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('Q1327','Akasa Air','Kolkata','Bengaluru',5000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('Q1313','Akasa Air','Chennai','Bengaluru',5500,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('Q1319','Akasa Air','Cochin','Chennai',5000,450,450);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E5307','IndiGo','Mumbai','Chennai',3000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E5303','IndiGo','Mumbai','Chennai',3500,750,750);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S6113','SpiceJet','Mumbai','Delhi',4000,550,550);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S2514','SpiceJet','Mumbai','Kolkata',3500,650,650);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('UK920','Vistara','Mumbai','Delhi',4000,550,550);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E2056','IndiGo','Mumbai','Delhi',4500,750,750);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E2111','IndiGo','Mumbai','Delhi',4000,350,350);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E2083','IndiGo','Mumbai','Delhi',4500,750,750);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8319','GO FIRST','Mumbai','Delhi',4000,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8327','GO FIRST','Mumbai','Delhi',4500,550,550);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8329','GO FIRST','Mumbai','Delhi',4700,550,550);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S8263','SpiceJet','Delhi','Kolkata',4000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S8253','SpiceJet','Delhi','Kolkata',7500,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E5353','IndiGo','Delhi','Kolkata',8000,550,550);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8101','GO FIRST','Delhi','Kolkata',6500,750,750);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6903','IndiGo','Delhi','Chennai',4000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8336','GO FIRST','Delhi','Chennai',7500,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8354','GO FIRST','Delhi','Chennai',8000,550,550);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('I5821','AirAsia India','Chennai','Bengaluru',4000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('I5612','AirAsia India','Chennai','Bengaluru',7500,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('I5146','AirAsia India','Chennai','Bengaluru',8000,550,550);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('Q1316','Akasa Air','Chennai','Bengaluru',6500,750,750);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('Q1322','Akasa Air','Chennai','Bengaluru',4000,450,450);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('AI785','Air India','Kolkata','Chennai',7500,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6214','IndiGo','Kolkata','Chennai',8500,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E7561','IndiGo','Kolkata','Chennai',8000,450,450);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('AI800','AirAsia India','Kolkata','Chennai',8000,450,450);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8227','GO FIRST','Kolkata','Delhi',5500,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8102','GO FIRST','Kolkata','Delhi',6500,750,750);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6917','IndiGo','Kolkata','Delhi',6000,500,500);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S8264','SpiceJet','Kolkata','Delhi',6500,450,450);

insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S2421','SpiceJet','Kolkata','Mumbai',8500,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('S4891','SpiceJet','Kolkata','Mumbai',9500,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6717','IndiGo','Kolkata','Mumbai',9000,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('E6215','IndiGo','Kolkata','Mumbai',9500,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8514','GO FIRST','Kolkata','Mumbai',7000,650,650);
insert into flight (flight_number, flight_name, origin, destination, fare, total_seats, available_seats)
values ('G8512','GO FIRST','Kolkata','Mumbai',7500,650,650);

-- insert data to booking table
insert into booking (booked_by,flight_number,booking_date,travel_date,id_proof,passenger_name_1,passenger_age_1,passenger_name_2,passenger_age_2,passenger_name_3,passenger_age_3,total_fare,booking_status) 
values(8741098523,'G8227',current_date(),'2022-12-24','AAIDD2341H','Raj',23,'Ram',35,'Hari',54,15000.00,'Booked');
insert into booking (booked_by,flight_number,class_type,booking_date,travel_date,id_proof,passenger_name_1,passenger_age_1,passenger_name_2,passenger_age_2,passenger_name_3,passenger_age_3,total_fare,booking_status) 
values(9785686734,'G8514',current_date(),'2022-12-24','AAIDD2341H','Raj',23,'Ram',35,'Hari',54,15000.00,'Booked');
insert into booking (booked_by,flight_number,class_type,booking_date,travel_date,id_proof,passenger_name_1,passenger_age_1,passenger_name_2,passenger_age_2,passenger_name_3,passenger_age_3,total_fare,booking_status) 
values(8741098523,'G8512',current_date(),'2022-12-24','AAIDD2341H','Raj',23,'Ram',35,'Hari',54,15000.00,'Booked');

select last_insert_id(); 

select * from admin;
select * from customer;
select * from flight;
select * from booking;

update booking set travel_date = '2023-10-26' where booking_id = 1001;

show databases;