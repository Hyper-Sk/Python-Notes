import datetime

# get date and time ------->

x = datetime.datetime.now()
print(x)

# The date contains year, month, day, hour, minute, second, and microsecond.

# all methods to get specific data.

print(x.day)
print(x.month)
print(x.year)
# or you can use symbols to get data specifically 
print(x.strftime("%A"))


print("-------___-_-___------")


# set get and time -------->

# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

y = datetime.datetime(2020, 5, 17)
print(y)