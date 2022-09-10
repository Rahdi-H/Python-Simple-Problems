import datetime

def findAge(b_year, b_month, b_day):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    c_year = datetime.date.today().year
    c_month = datetime.date.today().month
    c_day = datetime.date.today().day

    if b_day > c_day:
        c_month -= 1
        c_day = c_day + months[b_month - 1]

    if b_month > c_month:
        c_year -= 1
        c_month += 12

    calculated_day = c_day - b_day
    calculated_month = c_month - b_month
    calculated_year = c_year - b_year

    present_age = f'you are {calculated_year} years {calculated_month} month {calculated_day} old'
    print(present_age)


findAge(2000, 8, 16)