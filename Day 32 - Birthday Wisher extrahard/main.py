##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
from smtplib import *

USERNAME = "email@domain.xyz"
PASSWORD = "***************"


# 1. Update the birthdays.csv
with open("birthdays.csv") as birthday_file:
    birthday_list = pandas.read_csv(birthday_file)
    birthday_dict = birthday_list.to_dict(orient="record")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for entry in birthday_dict:
    if entry["day"] == now.day and entry["month"] == now.month:
        todays_bday = entry
        birthday = True

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if birthday:
    new_letter = open(f"letter_to_{todays_bday['name']}.txt", "+w")
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        new_text = letter.replace("[NAME]", todays_bday["name"])
        new_letter.write(new_text)

# 4. Send the letter generated in step 3 to that person's email address.
    with open(f"letter_to_{todays_bday['name']}.txt", "r") as new_letter:
        read_letter = new_letter.read()
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(USERNAME, PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs=todays_bday["email"], msg=f"Subject:Happy Birthday\n\n{read_letter}")



