def check_leap(year):
    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        return True
    else:
        return False

time = list(map(str, input().split()))
#print(time)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t_year = int(time[2])
t_month = time[0]
t_day = int(time[1].split(sep=',')[0])
t_hour = int(time[3].split(sep=':')[0])
t_min = int(time[3].split(sep=':')[1] )
#print(t_hour)
if check_leap(t_year) == True:
    months_day[1] = 29
total_min = sum(months_day) * 24 * 60
sum_min = (sum(months_day[:months.index(t_month)]) + t_day - 1) * 24 * 60 + t_hour * 60 + t_min
#print(sum_min)
print(sum_min / total_min * 100)