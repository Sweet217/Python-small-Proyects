import sqlite3

# Task 1: Create connection object # This need to be your path where you have the database.
con = sqlite3.connect("/home/gabriel/Desktop/New Laptop semestre 2/Hotel database manipulation/hotel_booking.db")

# Task 2: Create cursor object
cur = con.cursor()

# Task 3: Create booking_summary table
cur.execute('''CREATE TABLE IF NOT EXISTS booking_summary
               (num INTEGER,
                hotel TEXT,
                is_cancelled INTEGER,
                lead_time INTEGER,
                arrival_date_year INTEGER,
                arrival_date_month TEXT,
                arrival_date_day_of_month INTEGER,
                adults INTEGER,  
                children INTEGER,
                country TEXT,
                adr REAL,
                special_requests INTEGER)''')

# Task 4: Insert sample data into booking_summary
cur.execute('''INSERT INTO booking_summary 
               VALUES (1, 'Resort Hotel', 0, 342, 2015, 'July', 1, 2, 0, 'BRA', 96.43, 0)''')
cur.execute('''INSERT INTO booking_summary 
               VALUES (2, 'City Hotel', 1, 13, 2017, 'May', 23, 1, 0, 'GBR', 100.24, 0)''')
cur.execute('''INSERT INTO booking_summary 
               VALUES (3, 'Resort Hotel', 0, 93, 2016, 'December', 3, 2, 0, 'USA', 127.84, 1)''')
cur.execute('''INSERT INTO booking_summary 
               VALUES (4, 'City Hotel', 0, 27, 2018, 'June', 18, 1, 0, 'BRA', 75.60, 0)''')
cur.execute('''INSERT INTO booking_summary 
               VALUES (5, 'Resort Hotel', 1, 8, 2019, 'August', 12, 2, 1, 'BRA', 220.50, 1)''')

# Task 5: Commit changes and close the connection
con.commit()
con.close()
