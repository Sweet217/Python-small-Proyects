# Import module 
import sqlite3

# Task 1: Create connection object
con = sqlite3.connect("/home/gabriel/Desktop/New Laptop semestre 2/Hotel database manipulation/hotel_booking.db")

# Task 2: Create cursor object
cur = con.cursor()

# Task 3: View first row of booking_summary
first_row = cur.execute('''SELECT * FROM "booking_summary"''').fetchone()
#print(first_row) Just a test

# Task 4: View first ten rows of booking_summary 
ten_rows = cur.execute('''SELECT * FROM "booking_summary"''').fetchmany(10)
#print(ten_rows) Just a test

# Task 5: Create object bra and print first 5 rows to view data
bra = cur.execute('''SELECT * FROM booking_summary WHERE country = 'BRA';''').fetchmany(5)
#print(bra) Just a test

# Task 6: Create new table called bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers
(
                   num INTEGER,
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

# Task 7: Insert the object bra into the table bra_customers 
cur.executemany('''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# Task 8: View the first 10 rows of bra_customers
ten_rows_bra = cur.execute('''SELECT * FROM "bra_customers"''').fetchmany(10)
#print(ten_rows_bra) Just a test =)

# Task 9: Retrieve lead_time rows where the bookings were canceled
lead_time_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;''').fetchall()

# Task 10: Find average lead time for those who canceled and print results
average_can = cur.execute('''SELECT AVG(lead_time) FROM bra_customers WHERE is_cancelled = 1;''').fetchone()
print("Average lead time for those who canceled {}".format(average_can))

# Task 11: Retrieve lead_time rows where the bookings were not canceled
lead_time_not_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

# Task 12: Find average lead time for those who did not cancel and print results
average_not_can = cur.execute('''SELECT AVG(lead_time) FROM bra_customers WHERE is_cancelled = 0;''').fetchone()
print("Average lead time for those who did not cancel{}".format(average_not_can))

# Task 13: Retrieve special_requests rows where the bookings were canceled
special_request_cancelled = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 1;''').fetchall()

# Task 14: Find total special requests for those who canceled and print results
average_special_cancelled = cur.execute('''SELECT (special_requests) FROM bra_customers WHERE is_cancelled = 1;''').fetchone()
print("Total special requests for those who canceled{}".format(average_special_cancelled))

# Task 15: Retrieve special_requests rows where the bookings were not canceled
special_request_not_cancelled = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

# Task 16: Find total speacial requests for those who did not cancel and print results
average_special_not_cancelled = cur.execute('''SELECT (special_requests) FROM bra_customers WHERE is_cancelled = 0;''').fetchone()
print("Total speacial requests for those who did not cancel{}".format(average_special_not_cancelled))

# Task 17: Commit changes and close the connection
con.commit()
con.close()


