# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
from dataclasses import dataclass
from datetime import datetime
import time
import pendulum
from termcolor import colored, cprint

# TODO: create a new datetime using pendulum
dt1 = pendulum.datetime(2022, 8, 20, tz="Europe/Kiev")
# print (dt1)
# print(isinstance(dt1, datetime))
# print (dt1.timezone.name)

# TODO: convert the time to another time zone

dt2 = dt1.in_timezone("Australia/Sydney")
# print (dt2)
# print (dt2.timezone.name)

# i1 = int(input("Input number of Australia time zones pls: "))
i=0
i1=5
for c in pendulum.timezones:
    if ("Australia" in c) and i<i1 and c !="Australia/ACT":
        message = colored('{}', 'yellow')
        print(message.format(c))
        i +=1

for c in pendulum.timezones:
    if "Kiev" in c:
        message = colored('{}', 'green')
        print(message.format(c))

       
print ("\n")

# TODO: create a new datetime using the now() function

dt3 =pendulum.now()
print(dt3.to_cookie_string())
print ("local time is:",dt3.timezone.name)

for c in pendulum.timezones:
    if "Kiev" in c:
        message = colored('found home timezone format - {}', 'green')
        print(message.format(c))
        dt4 = dt3.in_timezone(c)



message = colored('Time at Home - {}', 'red')

# print(message.format(dt4.to_date_string()))
# print(message.format(dt4.to_time_string()))
# print(message.format(dt4.to_datetime_string()))
# print(message.format(dt4.to_formatted_date_string()))
# print(message.format(dt4.to_cookie_string()))
# print(message.format(dt4.to_iso8601_string()))
# print(message.format(dt4.to_rfc822_string()))
# print(message.format(dt4.format("YYYY MM-DD HH:MM A")))

print(message.format(dt4.format("dddd DD MMMM YYYY HH:mm", locale="ru")))
# print('Time at Home', dt4.to_datetime_string())

# dt4 = dt4.add(minutes=560)

diff = dt4.diff_for_humans(dt3)
message = colored('Difference - {}', 'magenta')
print(message.format(diff))


# newdate = dt4.add(weeks=50)
# # print('Time at Home +30', newdate.to_datetime_string())
# message = colored('Time at Home +30 weeks - {}', 'blue')
# print(message.format(newdate.format("dddd DD MMMM YYYY HH:mm", locale="ru")))

today = pendulum.now()
birthday = pendulum.datetime(2023, 5, 31)

diff = today.diff(birthday).in_days()
print (diff, "day to Your birthsday")

