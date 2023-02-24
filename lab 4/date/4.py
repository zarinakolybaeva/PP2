import datetime as dt
a = dt.datetime(2021,12,30,23,59,59)
b = dt.datetime(2021,12,31,23,59,59)
c=b-a
print('Total difference in seconds: ', c.total_seconds())