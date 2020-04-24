import datetime
y=int(input())
day_of_year=int(input())
date0=datetime.datetime(y,1,1)
delta=datetime.timedelta(days=day_of_year-1)
date1=date0+delta
print(date1.month)
print(date1.day)