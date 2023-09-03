################################################################################
# Airlines reservation project                                                 #
# By Pranesh Umasankar                                                         #
################################################################################

# import built-in packages/modules
import datetime
from datetime import date

# import user defined packages/modules
import matplotlib.pyplot as plt
import pymysql

logged_role = ''
application_loop = True

# database connection
conn=pymysql.connect(host='localhost',user='root',password='PranesH',database='airlines')

if not conn:
    print('''Database connection failure, Possible errors are\n
            1 - MySQL server is not running\n
            2 - Database airlines does not exist''')
    exit(1)

cursor = conn.cursor()

############################################
# Login to the airlines reservation system #
# Login by admin or customer user          #
############################################
while True:
    print('+-------------------------------------------------+')
    print('|                    Main Menu                    |')
    print('+-------------------------------------------------+')
    print('| 1 --> Customer Sign In | 2 --> Customer Sign Up |')
    print('| 3 --> Admin Sign In    | 4 --> Forgot Password  |')
    print('|                        | 9 --> Exit             |')
    print('+-------------------------------------------------+')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        # customer sign in
        mobile_no = int(input('Enter mobile no.  : '))        
        
        sql_query = "select password from customer where mobile_no = %s;"
        values = (mobile_no)
        row_affected = cursor.execute(sql_query, values)       
        
        if row_affected >= 1:
            password = input('Enter password    : ')
            row = cursor.fetchall()
            if password == row[0][0]:
                logged_role = 'customer'
                print('Customer',mobile_no,'logged in successfully\n')
                
                sql_query = "update customer set logged_status = 'Y' where mobile_no = %s;"
                values = (mobile_no)
                cursor.execute(sql_query, values)
                
                conn.commit()
                break
            else:
                print('Wrong password\n')
        else:            
            print('Customer',mobile_no,'does not exist\n') 
    elif choice == 2:
        # customer sign up
        print('+-------------------------------------+')
        print('| Please enter customer details below |')
        print('+-------------------------------------+')
        mobile_no = int(input('Enter mobile no.        : '))
        sql_query = "select * from customer where mobile_no = %s"
        values = (mobile_no)
        row_returned = cursor.execute(sql_query, values)
        
        if row_returned >= 1:
            print('Customer',mobile_no,'is already exists')
        else:
            first_name = input('Enter firstname         : ').strip().title()
            last_name = input('Enter lastname          : ').strip().title()
            password = input('Enter password          : ')
            gender = input('Enter gender (M / F)    : ').strip().upper()
            dob = input('Enter dob (DD/MM/YYYY)  : ').strip()
            address1 = input('Enter address 1         : ').strip().title()
            address2 = input('Enter address 2         : ').strip().title()
            pin = int(input('Pin code (6 digit)      : '))

            # convert dob from DD/MM/YYYY into YYYY/MM/DD
            # database accepts YYYY/MM/DD format only
            dob = datetime.datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d')

            sql_query = """insert into customer (first_name, last_name, mobile_no,  
                         password, gender, dob, address1, address2, pin)
                         values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (first_name, last_name, mobile_no, password, gender, dob, address1, address2, pin)

            row_inserted = 0
            row_inserted = cursor.execute(sql_query, values)

            conn.commit()

            if row_inserted == 1:
                print('Customer',first_name,'created with given details successfully\n')
                continue
            else:
                print('Customer',first_name,'data did not insert into table\n')
    elif choice == 3:
        # admin sign in
        username = input('Enter username : ').strip().lower()        
        
        sql_query = "select password from admin where user_name = %s;"
        values = (username)
        row_returned = 0        
        row_returned = cursor.execute(sql_query, values)
        
        if row_returned >= 1:
            password = input('Enter password : ')
            row = cursor.fetchall()
            if password == row[0][0]:
                logged_role = 'admin'
                print(username + ' logged in successfully\n')
                
                sql_query = "update admin set logged_status = 'Y' where user_name = %s;"
                values = (username)
                cursor.execute(sql_query, values)
                
                conn.commit()
                break
            else:
                print('Wrong password\n')
        else:            
            print(username,'user does not exist')
    elif choice == 4:
        # forgot password
        mobile_no = int(input('Enter mobile no.        : '))
        dob = input('Enter dob (DD/MM/YYYY)  : ').strip()
        dob = datetime.datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d')
        
        sql_query = "select password from customer where mobile_no = %s and dob = %s"
        values = (mobile_no,dob)
        
        row_returned = 0
        row_returned = cursor.execute(sql_query, values)
        if row_returned >= 1:
            row = cursor.fetchall()
            print('Password for customer',mobile_no,'is :',row[0][0],'\n')
        else:
            print('Customer with given mobile nubmer or dob is not found, Please check and retry\n')        
        continue
    elif choice == 9:
        cursor.close()
        conn.close()
        application_loop = False
        print('Bye... Bye...')
        break
    else:
        print('Wrong choice, please try again\n')
        continue

while application_loop == True:
    if logged_role == 'admin':
        print('+----------------------------------------------------------------------+')
        print('|                             Admin Menu                               |')
        print('+----------------------------------------------------------------------+')
        print('| 1 --> Add Flight    | 2 --> Edit Flight     | 3 --> View Flight      |')
        print('| 4 --> Delele Flight | 5 --> Booking History | 6 --> (Un)Block Flight |')
        print('| 7 --> Graph         | 8 --> View Customer   | 9 --> Exit             |')
        print('+----------------------------------------------------------------------+')

        choice = int(input('Enter your choice : '))
        
        if choice == 1:
            # add flight
            print('+-----------------------------------+')
            print('| Please enter flight details below |')
            print('+-----------------------------------+')
            flight_number = input('Enter flight number : ').strip().upper()
            
            sql_query = "select * from flight where flight_number = %s"
            values = (flight_number)
            row_returned = cursor.execute(sql_query, values)
            
            if row_returned >= 1:
                print('Flight number',flight_number,'is already exists')
            else:            
                flight_name = input('Enter flight name   : ').strip().title()
                origin = input('Enter origin        : ').strip().title()
                destination = input('Enter destination   : ').strip().title()
                fare = float(input('Enter ticket fare   : '))
                total_seats = int(input('Enter total seats   : '))

                sql_query = """insert into flight (flight_number, flight_name, origin,  
                             destination, fare, total_seats, available_seats)
                             values(%s, %s, %s, %s, %s, %s, %s)"""
                values = (flight_number, flight_name, origin, destination, fare, total_seats, total_seats)

                row_inserted = 0
                row_inserted = cursor.execute(sql_query, values)

                conn.commit()

                if row_inserted == 1:
                    print('Flight',flight_number,'created with given details successfully\n')
                else:
                    print('Flight',flight_number,'did not create\n')
        elif choice == 2:
            # edit flight            
            flight_number = input('Enter flight number : ').strip().upper()
            sql_query = "select flight_id from flight where flight_number = %s;"
            values = (flight_number)
            row_affected = cursor.execute(sql_query, values)
            
            if row_affected >= 1:                
                row = cursor.fetchall()
                flight_id = row[0][0]      
                print('+-----------------------------------+')
                print('| Please enter flight details below |')
                print('+-----------------------------------+')                
                flight_name = input('Enter flight name   : ').strip().title()
                origin = input('Enter origin        : ').strip().title()
                destination = input('Enter destination   : ').strip().title()
                fare = float(input('Enter ticket fare   : '))
                total_seats = int(input('Enter total seats   : '))                

                sql_query = """update flight set flight_number = %s, flight_name = %s, origin = %s, destination = %s,
                            fare = %s, total_seats = %s, available_seats = %s where flight_id = %s;"""
                values = (flight_number,flight_name,origin,destination,fare,total_seats,total_seats,flight_id)
                
                row_updated = 0
                row_updated = cursor.execute(sql_query, values)
                
                conn.commit()
                
                if row_updated >= 1:
                    print('Flight id',flight_id,'details are updated successfully\n')
                else:
                    print('Flight id',flight_id,'details did not update\n') 
            else:
                print('Flight number',flight_number,'not found\n')            
        elif choice == 3:
            # view flight
            sql_query = "select * from flight;"
            row_returned = cursor.execute(sql_query)
            if row_returned >= 1:
                print('+--------------------------------------------------------------------------------------------------------+')
                print('|                                               Flight List                                              |')
                print('+------+--------+---------------+---------------+---------------+---------------+-------+-------+--------+')
                print('| Fid  | Flt No | Flight Name\t| Origin\t| Destination\t| Fare\t\t| T S\t| A S\t| Active |')
                print('+------+--------+---------------+---------------+---------------+---------------+-------+-------+------- +')                
                row = cursor.fetchall()
                for row_data in row:
                    print(f'| {row_data[0]} | {row_data[1]}  | {row_data[2]}\t| {row_data[3]}   \t| {row_data[4]}   \t| {row_data[5]}\t| {row_data[6]}\t| {row_data[7]}\t|   {row_data[8]}    |')            
                print('+------+--------+---------------+---------------+---------------+---------------+-------+-------+------- +\n')
            else:
                print('Flight table is empty')
        elif choice == 4:
            # delete flight
            flight_number = input('Enter flight number : ').strip().upper()

            # delete records from booking table
            sql_query = "delete from booking where flight_number = %s;"
            values = (flight_number)
            row_deleted = cursor.execute(sql_query, values)
            
            conn.commit()
            
            sql_query = "delete from flight where flight_number = %s;"
            values = (flight_number)
            row_affected = cursor.execute(sql_query, values)
            
            conn.commit()
            
            if row_affected >= 1:
                print('Flight number',flight_number,'is deleted successfully\n')
            else:
                print('Flight number',flight_number,'not found\n')            
        elif choice == 5:
            # booking list for a particular flight
            flight_number = input('Enter flight number : ').strip().upper()
            
            sql_query = "select * from booking where flight_number = %s;"
            values = (flight_number)
            row_returned = cursor.execute(sql_query, values)
            if row_returned >= 1:
                print('+---------------------------------------------------------------------------------------------------------------+')
                print('|                                           Booking List For A Flight                                           |')
                print('+--------+---------------+---------------+---------------+---------------+-------+---------------+--------------+')
                print('| Bid \t | Booked by \t | Flt No. \t | Booked Dt \t | Travel Dt \t | Passr | Total Fare \t | Status\t|')
                print('+--------+---------------+---------------+---------------+---------------+-------+---------------+--------------+')
                row = cursor.fetchall()
                for row_data in row:
                    booked_date = datetime.datetime.strptime(str(row_data[3]), '%Y-%m-%d').strftime('%d-%m-%Y')
                    travel_date = datetime.datetime.strptime(str(row_data[4]), '%Y-%m-%d').strftime('%d-%m-%Y')                    
                    print(f'| {row_data[0]} \t | {row_data[1]} \t | {row_data[2]} \t | {booked_date} \t | {travel_date} \t |   {row_data[6]} \t | {row_data[13]} \t | {row_data[14]}\t|')
                print('+--------+---------------+---------------+---------------+---------------+-------+---------------+--------------+\n')
            else:
                print('Flight number',flight_number,'booking history is empty\n')
        elif choice == 6:
            # block / unblock flight
            flight_number = input('Enter flight number                             : ').strip().upper()

            sql_query = "select flight_id from flight where flight_number = %s;"
            values = (flight_number)
            row_returned = cursor.execute(sql_query, values)
            
            if row_returned >= 1:
                block_unblock = input('Enter block or unblock(default) flight (B / U)  : ').strip().upper()
                if block_unblock == 'B':
                    is_active = 'N'
                elif block_unblock == 'U':
                    is_active = 'Y'
                else:
                    is_active = 'Y'
                
                sql_query = "update flight set is_active = %s where flight_number = %s;"
                values = (is_active, flight_number)
                row_returned = cursor.execute(sql_query, values)
                conn.commit()
                print('Flight',flight_number,'status updated successfully\n')
            else:
                print('Flight number',flight_number,'not found\n')
        elif choice == 7:
            # graph, number of flights with seatching capacity
            sql_query = "select total_seats from flight;"
            row_returned = cursor.execute(sql_query)
            if row_returned >= 1:
                flight_total_seats = []
                row = cursor.fetchall()
                for row_data in row:
                    flight_total_seats.append(row_data[0])
                plt.hist(flight_total_seats,bins=[0,250,500,750,1000],edgecolor='yellow')
                plt.title('Number of flights with seating capacity range')
                plt.xlabel('Flight Seats Range')
                plt.ylabel('Number of Flights')
                plt.xticks([0,250,500,750,1000])                
                plt.show()
        elif choice == 8:
            # view customer
            sql_query = "select customer_id,first_name,last_name,mobile_no,gender,dob,pin from customer;"
            row_returned = cursor.execute(sql_query)
            if row_returned >= 1:
                print('+-----------------------------------------------------------------------------------------+')
                print('|                                     Customer List                                       |')
                print('+--------+---------------+---------------+---------------+-------+---------------+--------+')
                print('| Cid \t | Firstname \t | Lastname \t | Mobile no \t | Gender| DOB  \t | PIN \t  |')
                print('+--------+---------------+---------------+---------------+-------+---------------+--------+')
                row = cursor.fetchall()
                for row_data in row:
                    dob = datetime.datetime.strptime(str(row_data[5]), '%Y-%m-%d').strftime('%d-%m-%Y')
                    print(f'| {row_data[0]} \t | {row_data[1]} \t | {row_data[2]} \t | {row_data[3]} \t |   {row_data[4]} \t | {dob} \t | {row_data[6]} |')
                print('+--------+---------------+---------------+---------------+-------+---------------+--------+\n')
            else:
                print('Customer table is empty')                
        elif choice == 9:
            sql_query = "update admin set logged_status = 'N' where user_name = %s;"
            values = (username)
            row_affected = cursor.execute(sql_query, values)
            
            conn.commit()
            
            cursor.close()
            conn.close()
            print('Bye... Bye...')
            break
        else:
            print('Wrong choice, Please retry\n')
    elif logged_role == 'customer':
        print('+-----------------------------------------------------------------------+')
        print('|                             Customer Menu                             |')
        print('+-----------------------------------------------------------------------+')
        print('| 1 --> Book Ticket     | 2 --> Cancel Ticket   | 3 --> Booking History |')
        print('| 4 --> Change Password | 5 --> Change Mobile   | 6 --> Update Profile  |')
        print('| 7 --> Delete Customer |                       | 9 --> Exit            |')
        print('+-----------------------------------------------------------------------+')
        choice = int(input('Enter your choice : '))
        if choice == 1:
            # book ticket
            origin = input('Enter origin        : ').title()
            destination = input('Enter destination   : ').title()
            sql_query = "select * from flight where origin = %s and destination = %s and is_active = 'Y'"
            values = (origin, destination)
            
            row_returned = 0
            row_returned = cursor.execute(sql_query, values)
            
            if row_returned == 0:
                print('There is no flight from',origin,'to',destination)
            else:
                print('+-------------------------------------------------------------------------------------------------------+')
                print('|                                      Available Flight List                                            |')
                print('+-------+---------------+---------------+---------------+---------------+---------------+-------+-------+')
                print('| Fid\t| Flt No\t| Flt Name\t| Origin\t| Destination\t| Fare\t\t| T S\t| A S\t|')
                print('+-------+---------------+---------------+---------------+---------------+---------------+-------+-------+')
                row = cursor.fetchall()
                for row_data in row:
                    print(f'|{row_data[0]}\t| {row_data[1]}\t\t| {row_data[2]}\t| {row_data[3]}\t| {row_data[4]}  \t| {row_data[5]}\t| {row_data[6]}\t| {row_data[7]}\t|')            

                print('+-------+---------------+---------------+---------------+---------------+---------------+-------+-------+\n')
                flight_number = input('Enter flight number             : ').strip().upper()

                sql_query = "select fare,available_seats from flight where flight_number = %s;"
                values = (flight_number)
                row_affected = cursor.execute(sql_query, values)
                
                if row_affected >= 1:
                    travel_date = input('Enter travel date (DD/MM/YYYY)  : ')
                    travel_date = datetime.datetime.strptime(travel_date, '%d/%m/%Y').strftime('%Y-%m-%d')
                    id_proof = input('Enter ID number from ID proof   : ').strip().upper()
                    row = cursor.fetchall()
                    total_passenger = int(input('Enter total passenger (1 to 3)  : '))
                    if total_passenger < 1 or total_passenger > 3:
                        print('Total number of passenger should be 1 to 3 only, please retry') 
                        total_passenger = int(input('Enter total passenger (1 to 3)  : '))
                    total_fare = row[0][0] * total_passenger
                    available_seats = row[0][1] - total_passenger                    

                    # create empty list for passenger name and age
                    passenger_name = [None,None,None]
                    passenger_age = [None,None,None]

                    for index in range(0,total_passenger):
                        passenger_name[index] = input('Enter Passenger name            : ').strip().title()
                        passenger_age[index] = int(input('Enter Passenger age             : '))

                    sql_query = """insert into booking (booked_by, flight_number, booking_date, travel_date, 
                                id_proof, total_passenger, passenger_name_1, passenger_age_1, passenger_name_2, passenger_age_2, 
                                passenger_name_3, passenger_age_3,total_fare,booking_status)
                                values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    values = (mobile_no, flight_number, date.today(), travel_date, id_proof, total_passenger,
                              passenger_name[0], passenger_age[0], passenger_name[1], 
                              passenger_age[1], passenger_name[2], passenger_age[2],total_fare,'Booked')

                    row_inserted = 0
                    row_inserted = cursor.execute(sql_query, values)

                    conn.commit()

                    if row_inserted >= 1:
                        print('Ticket booked successfully\n')
                        sql_query = "update flight set available_seats = %s where flight_number = %s;"
                        values = (available_seats, flight_number)
                        cursor.execute(sql_query, values)
                        conn.commit()                     
                    else:
                        print('Ticket did not book\n')                
                else:
                    print('Flight number',flight_number,'not found, Please check and retry\n')                
        elif choice == 2:
            # cancel ticket
            booking_id = input('Enter booking id : ')
            sql_query = "select total_passenger,flight_number from booking where booking_id = %s;"
            values = (booking_id)
            row_returned = cursor.execute(sql_query, values)
            if row_returned >= 1:
                row = cursor.fetchall()
                total_passenger = row[0][0]
                flight_number = row[0][1]
                
                sql_query = "update booking set booking_status = %s where booking_id = %s;"
                values = ('Cancelled', booking_id)
                row_affected = cursor.execute(sql_query, values)
                
                conn.commit()
                
                sql_query = "select available_seats from flight where flight_number = %s;"
                values = (flight_number)
                row_returned = cursor.execute(sql_query, values)
                
                if row_returned >= 1:
                    row = cursor.fetchall() 
                    available_seats = row[0][0]
                    available_seats = available_seats + total_passenger
                
                    sql_query = "update flight set available_seats = %s where flight_number = %s;"
                    values = (available_seats,flight_number)
                    row_affected = cursor.execute(sql_query, values)
                    
                    conn.commit()
                    
                    if row_affected >= 1:
                        print('Ticket cancelled successfully\n')
                    else:
                        print('Ticket did not cancel, due to unknown issue\n')
            else:
                print('Booking id',booking_id,'is not found')
        elif choice == 3:
            # booking history
            sql_query = "select * from booking where booked_by = %s;"
            values = (mobile_no)
            row_returned = cursor.execute(sql_query, values)
            if row_returned >= 1:
                print('+-----------------------------------------------------------------------------------------------+')
                print('|                                        Booking History                                        |')
                print('+-------+---------------+---------------+---------------+-------+---------------+---------------+')
                print('| Bid\t| Flt No. \t| Booked Dt\t| Travel Dt\t| Passr\t| Total Fare\t| Status\t|')
                print('+-------+---------------+---------------+---------------+-------+---------------+---------------+')
                row = cursor.fetchall()
                for row_data in row:
                    booked_date = datetime.datetime.strptime(str(row_data[3]), '%Y-%m-%d').strftime('%d-%m-%Y')
                    travel_date = datetime.datetime.strptime(str(row_data[4]), '%Y-%m-%d').strftime('%d-%m-%Y')                    
                    print(f'| {row_data[0]}\t| {row_data[2]} \t| {booked_date}\t| {travel_date}\t|   {row_data[6]}\t| {row_data[13]}\t| {row_data[14]}\t|')
                print('+-------+---------------+---------------+---------------+-------+---------------+---------------+\n')
            else:
                print('You did not book any ticket\n')
        elif choice == 4:
            # change password
            sql_query = "select password from customer where mobile_no = %s;"
            values = (mobile_no)
            row_returned = 0
            row_returned = cursor.execute(sql_query, values)
            
            if row_returned >= 1:
                row = cursor.fetchall()
                password = input('Enter old password : ')
                if password == row[0][0]:
                    new_password = input('Enter new password : ')
                    
                    sql_query = "update customer set password = %s where mobile_no = %s;"
                    values = (new_password,mobile_no)
                    cursor.execute(sql_query, values)
                    
                    conn.commit()
                    
                    print('Customer',mobile_no,'password changed successfully\n')
                else:
                    print('Wrong password\n')
            else:
                print('Customer with',mobile_no,'does not exist\n')                    
        elif choice == 5:
            # change mobile number
            dob = input('Enter dob dd/mm/yyyy : ').strip()
            dob = datetime.datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d')

            sql_query = "select customer_id from customer where mobile_no = %s and dob = %s;"
            values = (mobile_no,dob)

            row_returned = 0
            row_returned = cursor.execute(sql_query, values)
            if row_returned >= 1:
                row = cursor.fetchall()
                customer_id = row[0][0]
                new_mobile_no = int(input('Enter new mobile no. : '))
                
                sql_query = "update customer set mobile_no = %s where customer_id = %s;"                
                values = (new_mobile_no,customer_id)
                cursor.execute(sql_query, values)
                
                conn.commit()
                
                print('Customer mobile no.',mobile_no,'is changed to',new_mobile_no,'successfully')
                print('Please login with new mobile and continue\n')
                break
            else:
                print('Customer with given mobile nubmer or dob is not found, Please check and retry\n')            
        elif choice == 6:
            # update profile
            sql_query = "select customer_id from customer where mobile_no = %s;"
            values = (mobile_no)
            row_returned = cursor.execute(sql_query, values)
            
            if row_returned >= 1:                
                row = cursor.fetchall()
                customer_id = row[0][0]
                
                print('+-----------------------------------------+')
                print('| Please enter customer new details below |')
                print('+-----------------------------------------+')
                first_name = input('Enter firstname        : ').title()
                last_name = input('Enter lastname         : ').title()
                gender = input('Enter gender (M / F)   : ').upper()
                dob = input('Enter dob (DD/MM/YYYY) : ')
                address1 = input('Enter address 1        : ').title()
                address2 = input('Enter address 2        : ').title()
                pin = int(input('Pin code (6 digit)     : ')) 
            
                dob = datetime.datetime.strptime(dob, '%d/%m/%Y').strftime('%Y-%m-%d')
                
                sql_query = """update customer set first_name = %s, last_name = %s, gender = %s,
                             dob = %s, address1 = %s, address2 = %s, pin = %s where customer_id = %s;"""
                values = (first_name,last_name,gender,dob,address1,address2,pin,customer_id)
                
                row_updated = 0
                row_updated = cursor.execute(sql_query, values)
                
                conn.commit()
                
                if row_updated >= 1:
                    print('Customer',customer_id,'details are updated successfully\n')
                else:
                    print('Customer',customer_id,'details did not update\n')
            else:
                print('Customer',mobile_no,'is not found\n')
        elif choice == 7:
            # delete customer
            sql_query = "delete from customer where mobile_no = %s;"
            values = (mobile_no)
            row_deleted = cursor.execute(sql_query, values)            
            conn.commit()
            
            if row_deleted >= 1:       
                cursor.close()
                conn.close()
                print('Customer',mobile_no,'is logged out and deleted successfully\n')
                break                
            else:
                print('Customer',mobile_no,'is not available / deleted\n')                
        elif choice == 9:
            # logout
            sql_query = "update customer set logged_status = 'N' where mobile_no = %s;"
            values = (mobile_no)
            cursor.execute(sql_query, values)
            
            conn.commit()            
            
            cursor.close()
            conn.close()
            print('Bye... Bye...')
            break
        else:
            print('Wrong choice, Please retry\n')
