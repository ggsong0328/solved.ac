def check_leap(year):
    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False

t_year, t_month, t_day = map(int, input().split())
d_year, d_month, d_day = map(int, input().split())
month_30 = [4, 6, 9, 11]
month_31 = [1, 3, 5, 7, 8, 10, 12]

days = 0


if t_month in month_30:
    days += 30 - t_day
elif t_month in month_31:
    days += 31 - t_day
else:
    if check_leap(t_year) == True:
        days += 29 - t_day
    else:
        days += 28 - t_day
#print(days)

for month in range(t_month+1, 13):
    if month in month_30:
        days += 30
    elif month in month_31:
        days += 31
    else:
        if check_leap(t_year) == True:
            days += 29
        else:
            days += 28
#print(days)

for year in range(t_year+1, d_year):
    if check_leap(year) == True:
        days += 366
    else:
        days += 365
#print(days)

for month in range(1, d_month):
    if month in month_30:
        days += 30
    elif month in month_31:
        days += 31
    else:
        if check_leap(d_year) == True:
            days += 29
        else:
            days += 28

days += d_day

if t_year == d_year:
    if check_leap(t_year) == True:
        days -= 366
    else:
        days -= 365

if d_year - t_year > 1000:
    print('gg')
elif d_year - t_year == 1000:
    if d_month > t_month:
        print('gg')
    elif d_month == t_month:
        if d_day >= t_day:
            print('gg')
        else:
            print(f'D-{days}')
    else:
        print(f'D-{days}')
else:
    print(f'D-{days}')