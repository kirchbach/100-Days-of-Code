from smtplib import*
import datetime as dt
import random

my_gmail = "?????@gmail.com"
gmail_password = "**************"

my_yahoo = "??????????@yahoo.com"

with open("quotes.txt","r") as quotes:
    quote = quotes.readlines()
    ran_quote = quote[random.randrange(0,101)]




now = dt.datetime.now()
if now.weekday() == 0:
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=gmail_password)
        connection.sendmail(from_addr=my_gmail, to_addrs=my_yahoo, msg=f"Subject:Motivational Quote of the Day\n\n{ran_quote}")