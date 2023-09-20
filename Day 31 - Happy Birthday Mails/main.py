##################### Extra Hard Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
from random import choice
import pandas as pd

now = dt.datetime.now()
present_day = now.day
present_month = now.month
letter1 = "./letter_templates/letter_1.txt"
letter2 = "./letter_templates/letter_2.txt"
letter3 = "./letter_templates/letter_3.txt"
letters = [letter1, letter2, letter3]

def send_mail(message):
    print("Mail sent")
    print(message)

def pick_letter():
    with open(choice(letters)) as file:
        letter = file.read()
    return letter



birthdays = pd.read_csv("birthdays.csv")

for x in birthdays.itertuples():
    print(x)
    if present_day == x.day and present_month == x.month:
        print("----------Yey, picking letter")
        letter = pick_letter()
        letter = letter.replace("[NAME]", x.name)
        print(letter)



