import os
import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.getenv("EMAIL_ID")
MY_PASSWORD = os.getenv("EMAIL_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP(os.getenv("EMAIL_SMTP_SERVER"), int(os.getenv("EMAIL_PORT"))) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )