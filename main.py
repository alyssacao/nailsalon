import psycopg2
from datetime import datetime, timedelta
import random

conn = None
cur = None

try:
    conn = psycopg2.connect(database=  'NailSalon',
                        user= 'postgres',
                        host= '127.0.0.1',
                        password='thuydieuu3011',
                        port=  5432)

    cur = conn.cursor()
    
    # Table CUSTOMER
    delete_customer = 'DROP TABLE IF EXISTS customer'
    cur.execute(delete_customer)
    
    create_customer =  '''CREATE TABLE IF NOT EXISTS customer (
                            c_id     varchar(10) PRIMARY KEY,
                            firstname    VARCHAR(35) NOT NULL,
                            lastname    VARCHAR(35),
                            phonenumber numeric(10),
                            street VARCHAR(40),
                            zipcode NUMERIC(7),
                            gender VARCHAR(1))'''
    cur.execute(create_customer)
    
    insert_customer = ' INSERT INTO customer (c_id, firstname, lastname, phonenumber, street, zipcode, gender) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    insert_cvalue = [('1', 'Goldie', 'Montand', '2012224321', '5235 Ironwood Ln', '07026', 'F'),
                    ('2', 'Lauren', 'Hershey', '2014441313', '2360 Maxon Rd', '07631', 'F'),
                    ('3','Claudia', 'Hermes', '2458379473','3526 Long Rd', '23892', 'F'),
                    ('4','Tyler', 'Smith', '8273748383','5635 N Termian St','60061', 'M')
                    ]
    for records in insert_cvalue:
        cur.execute(insert_customer, records)
    
    # Table APPOINTMENT
    # Delete table appointment if exists
    delete_appt = ' DROP TABLE IF EXISTS appointment'
    cur.execute(delete_appt)
    
    # Define the "appointment" table structure if not already defined
    create_appt = """
    CREATE TABLE IF NOT EXISTS appointment (
        a_id SERIAL PRIMARY KEY,
        c_id VARCHAR(10),
        staffid INT,
        datetime TIMESTAMP,
        service VARCHAR(100),
        status VARCHAR(20)
    )
    """
    cur.execute(create_appt)
    
    # List of available services
    services = [
    'Regular Manicure', 'Nochip Manicure', 'Dip Manicure',
    'Acrylic Regular', 'Acrylic Nochip', 'Regular Pedicure',
    'Deluxe Pedicure', 'Pedicure + Add Nochip on Toes'
    ]

    # Generate and insert 100 sample appointments for different customers
    for _ in range(100):
        c_id = str(random.randint(1, 10))  # Random customer ID (adjust as needed)
        staffid = random.randint(101, 110)  # Random staff ID (adjust as needed)

    # Generate a random appointment datetime within a date range
        start_date = datetime(2023, 9, 25)
        end_date = datetime(2023, 12, 31)
        appointment_datetime = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        appointment_datetime = appointment_datetime.replace(hour=random.randint(8, 18),
                                                        minute=random.choice([0, 15, 30, 45]))

    # Randomly select one or more services for the appointment
        selected_services = random.choice(services)

        status = random.choice(['Scheduled', 'Completed', 'Cancelled'])  # Random status

    # SQL INSERT statement to add a new appointment
        insert_appointment = """
        INSERT INTO appointment (c_id, staffid, datetime, service, status)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING a_id
        """
        cur.execute(insert_appointment, (c_id, staffid, appointment_datetime, selected_services, status))
        appointment_id = cur.fetchone()[0]
        print(f"Inserted appointment with ID: {appointment_id} for customer ID: {c_id}")
       
    # Table TECHNICIAN
    # Delete table nailtechnician if exists
    delete_staff = 'DROP TABLE IF EXISTS nailtechnician'
    cur.execute(delete_staff)
    # Create table nailtechnician
    create_staff = ''' CREATE TABLE IF NOT EXISTS nailtechnician (
                        staffid  VARCHAR(10) NOT NULL PRIMARY KEY,
                        name     VARCHAR(35) NOT NULL,
                        specialty VARCHAR(35),
                        contactinfo  VARCHAR(35)) '''
                        
    cur.execute(create_staff)
    # Insert values into nailteachnician table
    insert_ntech = ' INSERT INTO nailtechnician (staffid, name, specialty, contactinfo) VALUES (%s, %s, %s, %s)'
    insert_ntechvalue =[('101','Joana Lee', 'Acrylic Nochip', '123-456-7890 123 W Heeth St'),
                        ('102','Olivia Hwang', 'Nochip Manicure', '324-422-4356 0923 W Talman St'),
                        ('104', 'Michael Brown', 'Acrylic Regular', '111-222-3333 101 S Maple Ln'),
                        ('105', 'Emily Davis', 'Deluxe Pedicure', '888-888-8888 222 W Birch St'),
                        ('106', 'David Wilson', 'Nochip Manicure', '333-444-5555 789 E Pine Ave'),
                        ('107', 'Olivia Martinez', 'Regular Pedicure', '666-777-8888 567 N Cedar Rd'),
                        ('108', 'James Anderson', 'Acrylic Nochip', '999-999-9999 345 S Oak Ave'),
                        ('109', 'Sophia Rodriguez', 'Add Nochip on Toes', '444-555-6666 456 W Maple Ln'),
                        ('110','Sarah Johnson', 'Dip Manicure', '987-654-3210 789 N Oak Rd')]
    for nt_value in insert_ntechvalue:
        cur.execute(insert_ntech, nt_value )
        print(f"Values are inserted")
        
    # Table SERVICE
    # Delete table services if exist
    delete_services = 'DROP TABLE IF EXISTS services'
    cur.execute(delete_services)
    
    # Create table services
    create_services= '''CREATE TABLE IF NOT EXISTS service (
                            s_id VARCHAR(100),
                            servicename VARCHAR(100),
                            description VARCHAR(500),
                            duration VARCHAR(35),
                            price VARCHAR(20)
                            )'''
    cur.execute(create_services)
    
    # Insert available services into services table
    insert_service = 'INSERT INTO service (s_id, servicename, description, duration, price) VALUES (%s, %s, %s, %s, %s)'
    insert_svalue = [('1','Regular Manicure','','30 mins','$20'),
                     ('2','Nochip Manicure','','50 mins','$40'),
                     ('3','Dip Manicure','','60 mins','$50'),
                     ('4','Acrylic Regular','','45 mins','$45'),
                     ('5','Acrylic Nochip','','60 mins','$55'),
                     ('6','Regular Pedicure','','30 mins','$35'),
                     ('7','Deluxe Pedicure','','60 mins','$60'),
                     ('8','Pedicure + Add Nochip on Toes','','50 mins','$55')]
    for values in insert_svalue:
        cur.execute(insert_service, values)
        
    
    
    
    conn.commit()
except Exception as error  :
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()