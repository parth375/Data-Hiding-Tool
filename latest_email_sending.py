from email.message import EmailMessage
import ssl
import smtplib
import random
import string
from new_email_file import auth_email

length = 12
letters_and_digits = string.ascii_letters + string.digits
result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))

user_email = auth_email

email_sender = 'adc00020101@gmail.com'
email_password = 'bsprzeixdikpdjgf'

email_receiver = user_email

subject = "Secret key for Extraction"
body = f"""
    key :- {result_str}
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())


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


