import sys

location = sys.path
print(location)

for i in location: print(i)

import calendar

leapdays  = calendar.leapdays(2000, 2050)
print(leapdays)
is_it_leap = calendar.isleap(2043)
print(is_it_leap)
what_is_the_date_today = calendar.day_name     
print(what_is_the_date_today)