import datetime

ymd = [int(i) for i in input().split()]
d = datetime.date(*ymd)
delta = (int(input()))
countedDate = d+datetime.timedelta(delta)
print(countedDate.year, countedDate.month, countedDate.day)