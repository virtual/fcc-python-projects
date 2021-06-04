import math

# given a certain day (0 = Monday) and duration (1 day)
# add the duration to the day #, and mod by 6 to return
# the updated day name

# Return the day name of an equivalent day index #
def getDayNameByNum(dayIndex):
  if (dayIndex == 0): 
    return 'Monday'
  elif (dayIndex == 1):
    return 'Tuesday'
  elif (dayIndex == 2):
    return 'Wednesday'
  elif (dayIndex == 3):
    return 'Thursday'
  elif (dayIndex == 4):
    return 'Friday'
  elif (dayIndex == 5):
    return 'Saturday'
  elif (dayIndex == 6):
    return 'Sunday'

# given a day of the week, return the day's index #
def getDayNum(day):
  day = (day).lower()
  if (day == 'monday'):
    return 0
  elif (day == 'tuesday'):
    return 1
  elif (day == 'wednesday'):
    return 2
  elif (day == 'thursday'):
    return 3
  elif (day == 'friday'):
    return 4
  elif (day == 'saturday'):
    return 5
  elif (day == 'sunday'):
    return 6

def convertToTime(hour, min, days=0, startDay=''):
  period = 'AM'
  dayStr = ''
  endDay = ''
  endDayNum = -1
  if (startDay != ''):
    endDayNum = getDayNum(startDay)
  hour12 = hour
  if hour >= 12:
    hour12 = hour%12
    period = 'PM'
  if hour12 == 0:
    hour12 = 12
  if days == 1:
    dayStr = ' (next day)'
  elif days > 1:
    dayStr = ' (' + str(days) + ' days later)'
  
  if endDayNum > -1:
    endDay = (endDayNum + days) % 7
    endDay = ', ' + getDayNameByNum(endDay)
  
  return f'{hour12}:{str(min).zfill(2)} {period}{endDay}{dayStr}'
  # return f'{hour}:{str(min).zfill(2)} {period} ({days} Days)'

def add_time(start, duration, startDay=''):
  start = start.split(" ")
  
  # split and convert array items to ints
  hours, mins = map(int,start[0].split(':'))
  dHours, dMins = map(int,duration.split(':'))

  if (start[1].lower() == 'pm'):
    # Time is afternoon
    hours = hours + 12

  # Need to check if the clock reaches midnight instead of duration being 24 hours
  # Well this is saying duration of hours (like 8 hour day) + startHours, so if
  # this over 24, it is the next day
  daysOf = math.floor((hours + dHours) / 24)
  
  # return f'h: {(hours + dHours)%24}, {dHours} | {math.floor((mins + dMins)/60)} |  m: {mins}, {dMins} - ({days} Days)'
  minsOf = (mins + dMins)%60 #R
  hoursOf = (hours + dHours)%24 + math.floor((mins + dMins)/60) #Could be more than 24
  
  if hoursOf >= 24:
    daysOf = daysOf + math.floor(hoursOf/24)
    hoursOf = hoursOf%24
  
  new_time = convertToTime(hoursOf, minsOf, daysOf, startDay)
  return new_time