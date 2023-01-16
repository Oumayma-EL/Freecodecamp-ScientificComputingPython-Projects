def add_time(start, duration ,day="" ):
  left_days=0
  global new_day
  global index
  days=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  # splitting the time 
  start_split1=start.split(":")
  start_split2=start_split1[1].split()
  # Defining the hours and the minutes 
  hour=int(start_split1[0])
  minute=int(start_split2[0])
  moment=start_split2[1]  
  # splitting the duration
  duration_split=duration.split(":")
  hour_duration=int(duration_split[0])
  minute_duration=int(duration_split[1])
  if moment=="PM":
    hour=hour+12
  sum_hours=hour+hour_duration
  sum_minutes=minute+minute_duration
  # Manipulating the minutes 
  if sum_minutes>=60:
    left_hours=((sum_minutes-(sum_minutes%60))/60)
    sum_minutes=sum_minutes%60
    sum_hours=int(sum_hours+left_hours)
  # manipulating the hours 
  if sum_hours>=24:
    left_days=int(((sum_hours-(sum_hours%24))/24))
    sum_hours=sum_hours%24
  # Manipulation of PM and AM
  if sum_hours==0 and sum_minutes>=0:
    sum_hours=12
    new_moment="AM"
  elif sum_hours == 12 and sum_minutes >= 0:
    new_moment = "PM"
  elif sum_hours > 12 and sum_minutes >= 0:
    new_moment = "PM"
    sum_hours = sum_hours - 12
  else:
    new_moment = "AM" 
  # the printing of how many days left:
  if left_days == 1:
    next_day = "next day"
  else:
    next_day = f"{left_days} days later"
  # print(next_day)
  # print(left_days)
  # print(sum_hours,sum_minutes, new_moment)
  # Manipulation of the days :
  if day.lower() in days:
    index=days.index(day.lower())
    if left_days==0:
      days=days*1
    elif left_days==1:
      days=days*2
    else:
      days=days*left_days
    
    for ele in days:
      if day==ele:
        break
    new_day=days[index+left_days]
    
  # The printing manipulation 
    
  if day.lower() in days:
    
    if left_days==0:
      new_time=f"{sum_hours}:".rjust(2, "0") + f"{sum_minutes}".rjust(2,"0") + f" {new_moment}, " + f"{day.capitalize()}"
      
    else:
      new_time=f"{sum_hours}:".rjust(2, "0") + f"{sum_minutes}".rjust(2,"0") + f" {new_moment}, " + f"{new_day.capitalize()} ({next_day})"

      
  else:
    
    if left_days==0:
      new_time=f"{sum_hours}:".rjust(2, "0") + f"{sum_minutes}".rjust(2, "0") + f" {new_moment}"
      
    else:
      new_time=f"{sum_hours}:".rjust(2, "0") + f"{sum_minutes}".rjust(2, "0") + f" {new_moment} ({next_day})"

  return new_time
