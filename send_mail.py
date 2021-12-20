import smtplib

def create_message(from_address, to_address, name, buy_for):
    return (f"""
    From: {from_address}
    To: {to_address}
    Subject: Secret Sandra!

    Hello {name},

    Please buy a well good present for {buy_for}.

    Good luck,
    Sandra"""
    )

def send_message(gmail_password, from_address, to_address, email_text):
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(from_address, gmail_password)
        smtp_server.sendmail(from_address, to_address, email_text)
        smtp_server.close()
        return "Email sent successfully!"
    except Exception as ex:
        return f"Something went wrong….\n{ex}"

if __name__ == "__main__":
    print("This aint a script")