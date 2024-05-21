# Python Program to display calander

import calendar

year = 2024
month = 1

# print(calendar.month(year, month))

# for whole year calender
for i in range(1, 13):
    print(calendar.month(year, month))
    month = month + 1
