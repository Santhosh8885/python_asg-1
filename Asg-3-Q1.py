from datetime import datetime,timedelta

today = datetime.today()
print("Today :",today)
tommorrow = today+timedelta(1)
print("Tomorrow :",tommorrow)
yesterday = today-timedelta(1)
print("Yesterday:",yesterday)