duration = int(input('Введите количество секунд '))

min = 60
hour = 3600
day = hour * 24
month = day * 30
year = month * 12

print(duration // min, 'мин', duration % min, 'сек')

hour_rem = duration % hour
min_hour = hour_rem // min
sec_hour = hour_rem % min

print(duration // hour, 'ч', min_hour, 'мин', sec_hour, 'сек')

day_rem = duration % day
hour_day = day_rem // hour
min_rem = day_rem % hour
min_day = min_rem // min
sec_day = min_rem % min


print(duration // day, 'дней', hour_day, 'ч', min_day, 'мин', sec_day, 'сек' )

month_rem = duration % month
day_month = month_rem // day
hour_rem = month_rem % day
hour_month = hour_rem // hour
min_rem = hour_rem % hour
min_month = min_rem // min
sec_month = min_rem % min

print(duration // month, 'мес', day_month, 'дней', hour_month, 'ч', min_month, 'мин', sec_month, 'сек')

year_rem = duration % year
month_year = year_rem // month
month_rem = year_rem % month
day_year = month_rem // day
hour_rem = month_rem % day
hour_year = hour_rem // hour
min_rem = hour_rem % hour
min_year = min_rem // min
sec_year = min_rem % min

print(duration // year, 'г', month_year, 'мес', day_year, 'дней', hour_year, 'ч', min_year, 'мин', sec_year, 'сек')






