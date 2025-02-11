def is_leap(year):
  """here it is a docstring and its gonna explain the purpose of 
   the function written """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
days = 0
def days_in_month(year,month):
  """it actually calculates if the year is leap or not . 
  if that is a leap year than it increases the day count of feb by 1"""  
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year)==False:
    days=int(month_days[month-1])
  elif is_leap(year)==True:
    if month==2:
      days = int(month_days[month-1]+1)
    else:
      days = int(month_days[month-1])
  return days    
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

""""hello 
its a multiline comments"""


