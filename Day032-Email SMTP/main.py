import smtplib
import datetime as dt
import random 
import pandas as pd

my_email='appinformation0907@gmail.com'
password="password"

today=(dt.datetime.now().month,dt.datetime.now().day)
birthday=pd.read_csv("birthdays.csv")

birthday_dict={(data_row['month'],data_row['day']):data_row for (index,data_row) in birthday.iterrows()}

if today in birthday_dict:
    random_number=random.randint(1,3)
    file_path=f"letter_templates/letter_{random_number}.txt"
    birthday_person=birthday_dict[today]
    with open(file=file_path,encoding="utf-8") as file:
        content=file.read()
        content=content.replace('[NAME]',birthday_person['name'])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person['email'],
                                msg=f"Subject:Happy Birthday\n\n{content}".encode("utf-8"))
