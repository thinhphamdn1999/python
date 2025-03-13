from random import choice
import smtplib
import datetime as dt

my_email = "thinhphu1234567@gmail.com"
password = "fzrhswqsitqiihdu"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="beni09082004@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email",
#     )

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
# print(year)

# date_of_birth = dt.datetime(year=1999, month=5, day=21, hour=4)
# print(date_of_birth)

# WEEK_DAYS = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     0: "Sunday",
# }

# now = dt.datetime.now()
# weekday = now.weekday()

# with open("quotes.txt") as quote_file:
#     all_quotes = quote_file.readlines()
#     quote = choice(all_quotes)

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="beni09082004@gmail.com",
#         msg=f"Subject:{WEEK_DAYS[weekday]}\n\n{quote}",
#     )
