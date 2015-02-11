#!/usr/bin/env python3
class MyRangeError(Exception):
  def __init__(self, value):
      self.value = value
  def __str__(self):
    return repr(self.value)
def get_time_date():
  year = get_data("year")
  while year == False: 
    year = get_data("year")
  month = get_data("month")
  while month == False: 
      month = get_data("month")
  day = get_data("day")
  while day == False:
    day = get_data("day")
  hour = get_data("hour")
  while hour == False:
    hour = get_data("hour")
  minute = get_data("minute") 
  while minute == False:
    minute = get_data("minute") 
  second = get_data("second")
  while second == False:
    second = get_data("second")
  print(str(year) + "-" + str(month) + "-" + str(day) + " " + str(hour) + ":" + str(minute) + ":" + str(second))

def get_data(name):
  if name == "year":
    try:
      year = int(input("year > "))
      if year < 0:
        raise MyRangeError('Year out of bounds')
      return year
    except MyRangeError as err:
        print(err)
        return False  
  elif name == "month":
    try:
      month = int(input("month > "))
      if month > 12 or month < 1:
        raise MyRangeError("Month out of Bounds")
      return month
    except MyRangeError as err:
      print(err)
      return False
  elif name == "day":
    try:
      day = int(input("day > "))
      if day > 31 or day < 1:
        raise MyRangeError("Day out of bounds")
      return day
    except MyRangeError as err:
      print(err)
      return False
  elif name == "hour":
    try:
      hour = int(input("hour > "))
      if hour > 23 or hour < 0:
        raise MyRangeError("Hour out of Bounds")
      return hour
    except MyRangeError as err:
      print(err)
      return False
  elif name == "minute":
    try:
      minute = int(input("minute > "))
      if minute > 59 or minute < 0:
        raise MyRangeError("Minute out of Bounds")
      return minute
    except MyRangeError as err:
      print(err)
      return False
  elif name == "second":
    try:
      second = int(input("second > "))
      if second > 59 or second < 0:
        raise MyRangeError("Second out of Bounds")
      return second
    except MyRangeError as err:
      print(err)
      return False
print("Select a function")
print("1. Date") 
choice = int(input(">"))
if choice == 1:
  get_time_date()
