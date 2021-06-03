import math

def convertToTime(hour, min, days):
  period = 'AM'
  dayStr = ''
  hour12 = hour
  if hour >= 12:
    hour12 = hour%12
    period = 'PM'
  if hour12 == 0:
    hour12 = 12
  if days == 1:
    dayStr = ' (next day)'
  elif days > 1:
    dayStr = ' (' + days + ' days later)'
  
  return f'{hour12}:{str(min).zfill(2)} {period}{dayStr}'
  # return f'{hour}:{str(min).zfill(2)} {period} ({days} Days)'

def add_time(start, duration):
  start = start.split(" ")
  
  # split and convert array items to ints
  hours, mins = map(int,start[0].split(':'))
  dHours, dMins = map(int,duration.split(':'))

  if (start[1].lower() == 'pm'):
    # Time is afternoon
    hours = hours + 12

  # Need to check if the clock reaches midnight instead of duration being 24 hours
  daysOf = math.floor((hours + dHours) / 24)
  # return f'h: {(hours + dHours)%24}, {dHours} | {math.floor((mins + dMins)/60)} |  m: {mins}, {dMins} - ({days} Days)'
  minsOf = (mins + dMins)%60 #R
  hoursOf = (hours + dHours)%24 + math.floor((mins + dMins)/60) #Could be more than 24
  
  
  new_time = convertToTime(hoursOf, minsOf, daysOf)
  return new_time