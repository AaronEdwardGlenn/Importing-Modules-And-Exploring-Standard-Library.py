# here we are importing something from the standard library
import random
import math
import datetime
import calendar
import os

courses = ['history', 'math', 'science', 'art']

random_courses = random.choice(courses)

print(random_courses)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today
print(today())

print(calendar.isleap(2020))

print(os.getcwd())   # this prints out the current working directory for where this file is located

# we can also create/delete/search files and all of that usign the os module

print(os.__file__)
