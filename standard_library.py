# here we are importing something from the standard library
import random
import math
import datetime
import calendar

courses = ['history', 'math', 'science', 'art']

random_courses = random.choice(courses)

print(random_courses)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today
print(today())

print(calendar.isleap(2020))
