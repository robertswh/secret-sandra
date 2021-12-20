import pandas as pd
import smtplib

from name_match import match_names
from send_mail import create_message, send_message

data = pd.read_csv('email_addresses.csv')

df = match_names(data)

from_address = 'from_address@gmail.com'
gmail_password = 'gmail_password'

for index, row in df.iterrows():
    email = create_message(from_address, row["email_address"], row["name"], row["buy_for"])
    print(send_message(gmail_password, from_address, row["email_address"], email))