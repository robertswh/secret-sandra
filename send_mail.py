import smtplib

sender = 'example@gmail.com'
receiver = 'example@gmail.com'

message = f"""From: From Person <{sender}>
To: To Person <{receiver}>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receiver, message)         
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")