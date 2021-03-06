import datetime as dt

# Getting hold of current date and time
now = dt.datetime.now()
print(now)

"""Getting hold of specific"""
hour = now.hour
day = now.day
time = now.time
day_of_week = now.weekday() # It starts counting from 0 so monday will be 0
print(day)
print(day_of_week)


# Setting our own date and time
our_datetime = dt.datetime(year=2002, month=9, day=8)
print(our_datetime)

# strftime: To get a particular format o date and time we use
"""To get the particulars of strftime visite https://www.w3schools.com/python/python_datetime.asp"""
print(now.strftime("%Y%m%d"))
