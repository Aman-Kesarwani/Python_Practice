from datetime import datetime
import time

# today_dt = datetime.datetime(2020, 07, 25)

custom_dt = datetime(2020, 7, 25)

now_dt = datetime.now()

print(now_dt)

date_frm_string = datetime.strptime("2020/07/09", "%Y/%m/%d")
print(date_frm_string)
month = date_frm_string.month
print("month", month)

print("timestamp", time.time())

dt_from_timestamp = datetime.fromtimestamp(time.time())

print(dt_from_timestamp)

print(f"{dt_from_timestamp.year}/{dt_from_timestamp.month}/{dt_from_timestamp.day}")


string_from_date = date_frm_string.strftime("%d/%m")
print(string_from_date)

dt1 = datetime(2020, 12, 1)
dt2 = datetime(2020, 12, 25)

if(dt1 > dt2):
    print("dt1 is greater")
else:
    print("dt2 is greater")
