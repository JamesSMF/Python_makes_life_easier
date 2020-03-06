from datetime import datetime
import re

def days_between(d1, d2):
   d1 = datetime.strptime(d1, "%Y%m%d")
   d2 = datetime.strptime(d2, "%Y%m%d")
   return abs((d2 - d1).days)

start_date = input("Please enter the first date (format: Year-Month-Day): ")
end_date = input("Please enter another date (format: Year-Month-Day): ")

start_date = re.sub("[^0-9]", "", start_date)
end_date = re.sub("[^0-9]", "", end_date)

# check if the date is in the correct format, so the program does not
# produce funny results
assert(len(start_date) == 8 and len(end_date) == 8)

print(abs(days_between(start_date, end_date)))
