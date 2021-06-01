def convertToTime(hour, min):
  period = 'AM'
  if hour > 12:
    hour = hour%12
    period = 'PM'
  return f'{hour}:{min} {period}'

def add_time(start, duration):
  start = start.split(" ")
  
  # split and convert array items to ints
  hours, mins = map(int,start[0].split(':'))
  dHours, dMins = map(int,duration.split(':'))

  if (start[1].lower() == 'pm'):
    # Time is afternoon
    hours = hours + 12

  hours = hours + dHours
  mins = mins + dMins
  
  new_time = convertToTime(hours, mins)
  return new_time