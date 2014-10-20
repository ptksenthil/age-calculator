import datetime

print('***************** AGE CALCULATOR *********************')

y=int(input('Enter your year of Birth'))
m=int(input('Enter your year of Month'))
d=int(input('Enter your year of Date'))

dob=datetime.date(y,m,d)
today=datetime.date.today()

r=today-dob

year=r.days//365

days=r.days % 365

print('YOUR AGE IS :) ..%d years %d days' % (year,days))

