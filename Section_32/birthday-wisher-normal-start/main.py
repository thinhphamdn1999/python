import smtplib
import pandas
import datetime as dt
import random

MY_EMAIL = "thinhphu1234567@gmail.com"
MY_PASSWORD = "fzrhswqsitqiihdu"
data_frame = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (
        data_row["month"],
        data_row["day"],
    ): (
        data_row["name"],
        data_row["email"],
        data_row["month"],
        data_row["day"],
    )
    for (_, data_row) in data_frame.iterrows()
}

today = (dt.datetime.now().month, dt.datetime.now().day)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letter_number = random.randint(1, 3)

    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthday_person[0])
        print(letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person[1],
            msg=f"Subject:Happy Birthday!\n\n{letter}",
        )
