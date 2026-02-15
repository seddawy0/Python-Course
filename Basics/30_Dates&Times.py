print("#################### Dates & Times #####################")
import datetime

date = datetime.date(year=2026, month=2, day=15)
time = datetime.time(hour=10, minute=42, second=30)
print(f"Date: {date}")
print(f"Time: {time}")
print("---------------------")
print()
today = datetime.datetime.today()
now = datetime.datetime.now()
print(f"Today: {today}")
print(f"Now: {now}")
print("---------------------")
print()
now = now.strftime("%m/%d/%Y : %H:%M:%S")
print(f"Formatted Now: {now}")
print("---------------------")
print()
target_time = datetime.datetime(year=2026, month=6, day=15)
current_time = datetime.datetime.now()
if target_time < current_time:
    print("Targer date has passed!")
else:
    remaining_time = target_time - current_time
    print("Targer date has NOT passed")
    print(F"Remaining days: {remaining_time.days}")
print("########################################################")