import datetime
def calculateAge(year, month, day):
    today = datetime.date.today()
    dob = datetime.date(year, month, day)
    age = float((today - dob).days / 365)
    return age


enterdob = input('enter dob in this format year-month-day')
a = enterdob.split('-')
year, month, day = int(a[0]), int(a[1]), int(a[2])
age = calculateAge(year, month, day)
print(f'you are {age} years old')