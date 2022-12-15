# Import module 
import sqlite3


# Task 1: Create connection object

con = sqlite3.connect("hotel_booking.db")

# Task 2: Create cursor object

curs = con.cursor()

# Task 3: View first row of booking_summary

first_row = curs.execute("SELECT * FROM booking_summary").fetchone()

#print(first_row)

# Task 4: View first ten rows of booking_summary 

ten_rows = curs.execute("SELECT * FROM booking_summary").fetchmany(10)

#print(ten_rows)

# Task 5: Create object bra and print first 5 rows to view data

bra = curs.execute("SELECT * FROM booking_summary WHERE country = 'BRA'").fetchall()

#print(bra)

# Task 6: Create new table called bra_customers

curs.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
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
  special_requests INTEGER
)''')

# Task 7: Insert the object bra into the table bra_customers 

curs.executemany('''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# Task 8: View the first 10 rows of bra_customers

bra_ten = curs.execute("SELECT * FROM bra_customers").fetchmany(10)

#print(bra_ten)

# Task 9: Retrieve lead_time rows where the bookings were canceled

lead_time_can = curs.execute("SELECT * FROM bra_customers WHERE is_cancelled = 0").fetchall()

# Task 10: Find average lead time for those who cancelled and print results

sum_cancelled = 0
for lead_time in lead_time_can:
  sum_cancelled += lead_time[3]

average_lead_time_can = sum_cancelled / len(lead_time_can)
print(average_lead_time_can)

# Task 11: Retrieve lead_time rows where the bookings were not cancelled

lead_time_not_can = curs.execute("SELECT * FROM bra_customers WHERE is_cancelled = 1").fetchall()

# Task 12: Find average lead time for those who did not cancel and print result

sum_not_cancelled = 0
for lead_time in lead_time_not_can:
  sum_not_cancelled += lead_time[3]

average_lead_time_not_can = sum_not_cancelled / len(lead_time_not_can)
print(average_lead_time_not_can)

# Task 13: Retrieve special_requests rows where the bookings were canceled

special_requests_can = curs.execute("SELECT special_requests FROM bra_customers WHERE is_cancelled = 0").fetchall()

# Task 14: Find total special requests for those who canceled and print results

total_requests_can = 0
for request in special_requests_can:
  total_requests_can += request[-1]

print(total_requests_can)

# Task 15: Retrieve special_requests rows where the bookings were not canceled

special_requests_not_can = curs.execute("SELECT special_requests FROM bra_customers WHERE is_cancelled = 1").fetchall()

# Task 16: Find total speacial requests for those who did not cancel and print results

total_requests_not_can = 0

for request in special_requests_not_can:
  total_requests_not_can += request[-1]

print(total_requests_not_can)

# Task 17: Commit changes and close the connection

con.commit()

con.close()