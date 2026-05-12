import smtplib
import datetime
import random

#CONSTANTS
MY_EMAIL = ""
RECIPIENT_EMAIL = ""
EMAIL_AUTH = ""
EMAIL_SUBJECT = "Have a Great Day"
SMTP_SERVER = ""

now = datetime.datetime.now()
current_day_of_the_week = now.weekday()

with open("./quotes.txt") as file:
    quotes = [quotes.strip() for quotes in file]

def send_quote():
    quote_to_send = quotes[random.randint(0, len(quotes) - 1)]
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_AUTH)
        connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=RECIPIENT_EMAIL,
        msg=f"Subject:{EMAIL_SUBJECT}\n\n"
            f"{quote_to_send}"
    )

if current_day_of_the_week == 1:
    send_quote()


