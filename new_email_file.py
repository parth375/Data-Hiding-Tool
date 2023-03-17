# auth_email = input("Enter your email for Authentication:- ")

# Final file for inserting email at the time of decryption/extraction

import mysql.connector

db1 = mysql.connector.connect(host = 'localhost', user='root',
password='#aditya', database = 'users')

# print("Connection Successful")

cur = db1.cursor()      # help in execute our db query

auth_email = input("Enter your email for Authentication:- ")

# create_query = 'CREATE TABLE details(Email Varchar(200))'
check_query = 'select * from details where email = %s'

data = (auth_email,)

# data = (user_input,)

cur.execute(check_query, data)

rows = cur.fetchall()

if len(rows) == 0:
    print("Email does not exists")

else:
    import latest_email_sending as se
    from latest_email_sending import *

















# filename = open("email.txt")
#
# if(auth_email in filename.read()):
#     import latest_email_sending as se
#     from latest_email_sending import *
#
# else:
#     print("Email not Found!!!")