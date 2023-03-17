#
# em_or_ex = input("embed(e) or extract(d)")
#
# filename = open("email.txt")
# if(em_or_ex == 'e'):
#     email = input("Enter your email.")
#     with open("email.txt",'a') as f:
#         f.write('\n')
#         f.write(email)

# else:
#     authenticate = input("enter your email.")
#     if(authenticate in filename.read()):
#         print("Authenticated")
#     else:
#         print("Email not found!")



import random
import string
import smtplib,ssl
from new_email_file import auth_email

user_email = auth_email

# For sending an email to authentic person, below code is used.
length = 12
letters_and_digits = string.ascii_letters + string.digits
result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
# print("Secret key is:", result_str)

sender_email = "adc00020101@gmail.com"
receiver_email = user_email
message = f"""\
Subject: Hi there
{result_str}
"""

# Send email here

port = 465  # For SSL
password = "@d!ty@$7654567"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("sender_email", password)
    # TODO: Send email here

    server.sendmail(sender_email, receiver_email, message)

ask_user = input("Enter key that you have got in your email:-  ")

if(ask_user == result_str):
    print("Key matched!!!")

    import HIDE_IMG_YT as yt    # These are the modules/files that are used for extracting file from the image
    from HIDE_IMG_YT import *

    import unzip_file as uf
    from unzip_file import *

    import f_decrypt as fd
    from f_decrypt import *

else:

    print("Key not matched.")




