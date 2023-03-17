# Final file for inserting email at the time of decryption/extraction

import mysql.connector

db1 = mysql.connector.connect(host = 'localhost', user='root', 
password='#aditya', database = 'users')

# print("Connection Successful")

cur = db1.cursor()      # help in execute our db query

user_input = input("Enter your email address!")

# create_query = 'CREATE TABLE details(Email Varchar(200))'
check_query = 'select * from details where email = %s'

data = (user_input,)

# data = (user_input,)

cur.execute(check_query, data)

rows = cur.fetchall()

if len(rows) == 0:
    print("Email does not exists")

else:
    print("Email Exists")










