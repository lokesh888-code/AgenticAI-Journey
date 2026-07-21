from datetime import datetime

print("Current date and time:", datetime.now())
print("Current year:", datetime.now().year)
print("Current month:", datetime.now().month)
print("Current day:", datetime.now().day)
print("Current hour:", datetime.now().hour)
print("Current minute:", datetime.now().minute)
print("Current second:", datetime.now().second)
print("Current date:", datetime.now().date())
print("Custome date format:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))