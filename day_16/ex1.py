from datetime import datetime
tm=datetime.now()
print(tm)
print(tm.strftime("%m/%d/%Y, %H:%M:%S"))
st="5 December, 2019"
print(datetime.strptime(st,"%d %B, %Y"))

date2=datetime(2026,1,1)
print(date2 - tm)

print(datetime.now().timestamp())