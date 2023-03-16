print("A clock was reading the time accurately on Friday at noon. On Monday at 6pm the clock was running late by 468 seconds. On average, how many seconds did the clock skip every 30 minutes?")

#values

one_day = 24 #hours
one_hour = 60 #minutes
half_hour = 30

#find the total hours to then be converted to half hours inbetween Friday 6pm to Mon 6pm
total_hours = 12+24+24+18
total_hours_in_half_hours = total_hours*2

print("Friday 12pm > Saturday 12am took 12 hours > Sunday 12am took 24 hours > Monday 12am took 24 hours > Monday 6pm took 18 hours")
print(f"12+24+24+18 = {total_hours}")

print(f"There was {total_hours} hours from Friday 12pm to Monday 6pm.")
print(f"There was {total_hours_in_half_hours} half hours from Friday 12pm to Monday 6pm.")

x = 468/total_hours_in_half_hours #seconds
print(f"There clock was running late by 468 seconds. We then divide it by 156 to convert the half hours into seconds.")
print(f"The clock skipped {x} seconds for every 30 minutes from Fri 12pm to Mon 6pm.")
