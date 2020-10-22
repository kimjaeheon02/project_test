from datetime import date, timedelta

today = date.today()

print(today)

first_day = today.replace(month=today.month+1, day=1)
last_day = first_day-timedelta(days=1)
print(last_day.day)

for i in range(1, last_day.day+1):
    print(i, end=' ')
