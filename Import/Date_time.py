import datetime as dt

'''now=dt.datetime.now()
print("Now: ",now)
print("Today: ",dt.datetime.today())
'''
# custom datetime
'''a=dt.datetime(2022,12,28)
print(a)
b=dt.datetime(2007,9,5,4,10,12,93458)
print("My birth time: ",b)
'''
# current date 
'''current_date=dt.date.today()
print("cuurent_year: ",current_date.year)
print("current_Month: ",current_date.month)
print("current_Day: ",current_date.day)
'''

T1= dt.time()
print("Default time: ",T1)

t2=dt.time(minute=12,hour=12,second=13,microsecond=23451)
print("Custom Time: ",t2)

t3=dt.time(11,34,56,23453)
print("Full Time: ",t3)
