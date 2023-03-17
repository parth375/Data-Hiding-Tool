# Final file for inserting email at the time of encryption/embedding

import mysql.connector

db1 = mysql.connector.connect(host = 'localhost', user='root',
password='#aditya', database = 'users')

# print("Connection Successful")

cur = db1.cursor()      # help in execute our db query

user_input = input("Enter your email address!")

# create_query = 'CREATE TABLE details(Email Varchar(200))'
insert_query = 'INSERT INTO details values(%s)'
check_query = 'select * from details where email = %s'

data = (user_input,)

cur.execute(check_query, data)

rows = cur.fetchall()

if len(rows) == 0:
   cur.execute(insert_query,data)

db1.commit()            # It is used to save the changes in database




