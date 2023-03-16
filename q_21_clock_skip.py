#Change the question here

print("A clock was reading the time accurately on Tuesday at noon. On Thursday at 3pm the clock was running late by 612 seconds. On average, how many seconds did the clock skip every 30 minutes?")

#Hard code the values here

one_day = 24 #hours
one_hour = 60 #minutes
half_hour = 30
seconds_running_late = 612

#Find and hard code the respective hours for every day inbetween Tues 12pm to Thurs 3pm
total_hours = 12+24+15
total_hours_in_half_hours = total_hours*2

print("Friday 12pm > Saturday 12am took 12 hours > Sunday 12am took 24 hours > Monday 12am took 24 hours > Monday 6pm took 18 hours")
print(f"12+24+15 = {total_hours}")

print(f"There was {total_hours} hours from Tuesday 12pm to Thursday 3pm.")
print(f"Or {total_hours_in_half_hours} in half hours.")


x = seconds_running_late/total_hours_in_half_hours #seconds
print(f"There clock was running late by {seconds_running_late} seconds. We then divide it by {total_hours_in_half_hours} to convert the half hours into seconds.")
print(f"The clock skipped {x} seconds for every 30 minutes from Tuesday 12pm to Thursday 3pm.")
