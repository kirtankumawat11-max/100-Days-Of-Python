import datetime as dt
import pandas
import random
import smtplib

my_email = "check91052@gmail.com"
password = "jakztynnecpvjoll"

today_touple = (dt.datetime.now().month,dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]) : data_row for (index,data_row) in data.iterrows()}

if today_touple in birthdays_dict :
    birthdays_person = birthdays_dict[today_touple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection :
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents} "
        )