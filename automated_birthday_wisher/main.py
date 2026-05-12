#create automatic birthday wisher
import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = ""
EMAIL_AUTH = ""
SMTP_SERVER = ""
EMAIL_SUBJECT = "Happy Birthday"

now = dt.datetime.now()
today = (now.month, now.day)

birthdays = pd.read_csv("./birthdays.csv")

for index, row in birthdays.iterrows():
    if  birthdays.iloc[index, 3] == today[0]:
        if birthdays.iloc[index, 4] == today[1]:
            with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
                temp_letter = letter.read()
            finished_letter = temp_letter.replace("[NAME]", birthdays.iloc[index, 0])
            with smtplib.SMTP(SMTP_SERVER) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=EMAIL_AUTH)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthdays.iloc[index, 1],
                    msg=f"Subject:{EMAIL_SUBJECT}\n\n"
                        f"{finished_letter}"
                )
