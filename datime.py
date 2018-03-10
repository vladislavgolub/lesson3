import time
from datetime import datetime, timedelta
import locale

date_today = datetime.now()
delta1 = timedelta(days = 1)
delta2 = timedelta(days = 28)
date_today = date_today.date()

date_tomorrow = date_today + delta1
date_month_ago = date_today - delta2
print('Сегодня: ',date_today)
print('Завтра: ',date_tomorrow)
print('Месяц назад (актуально для марта): ',date_month_ago)

string = '01/01/17 12:10:03.234567'
datetime_microsec = string.split('.')
datetime_str = datetime_microsec[0]

datetime_str = datetime.strptime(datetime_str,'%d/%m/%y %H:%M:%S')

microsec = int(datetime_microsec[1])
result = datetime_str.replace(microsecond=microsec)
print(result, type(result)) #type для проверки того, что я переписал строку в datetime