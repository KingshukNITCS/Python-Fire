import math
result = math.ceil(4.2)
print(result)  


 import math
 result = math.floor(4.9)
 print(result)

import math
result = math.trunc(4.9)
print(result) 



import math
result = math.sqrt(16)
print(result)


import math
angle = math.radians(45)  # Convert degrees to radians
sin_result = math.sin(angle)
cos_result = math.cos(angle)
tan_result = math.tan(angle)
print("sin_result :",sin_result, "cos_result :", cos_result, "tan_result :", tan_result)


import math
result = math.log(16, 2)
print(result)  


   import math
   result = math.exp(2)
   print(result)


import math
print(math.pi)
print(math.e)

import random
value = random.random()
print(value)


import random
value = random.randint(1, 10)
print(value)


import random
value = random.uniform(1.0, 5.0)
print(value)


import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)


import random
my_list = [1, 2, 3, 4, 5]
value = random.choice(my_list)
print(value)


import random
my_list = [1, 2, 3, 4, 5]
sampled = random.sample(my_list, 3)
print(sampled)



from datetime import datetime
current_datetime = datetime.now()
print(current_datetime)


from datetime import date
current_date = date.today()
print(current_date)


from datetime import datetime
current_datetime=datetime.now()
# Format a datetime object as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Parse a string into a datetime object
parsed_date = datetime.strptime("2023-01-01 12:30:00", "%Y-%m-%d %H:%M:%S")
print(parsed_date)


from datetime import datetime, timedelta
current_datetime=datetime.now()
future_date = current_datetime + timedelta(days=7)
print(future_date)


# Problem Statement - Write a Python program that calculates the remaining days, hours, and minutes until the event. Additionally, provide the percentage completion of the event based on the current time compared to the event's start time.
from datetime import datetime, timedelta
import math

event_date = datetime(2023, 12, 31, 18, 30)  # December 31, 2023, 6:30 PM

current_datetime = datetime.now()

time_difference = event_date - current_datetime
remaining_days = time_difference.days
remaining_hours, remaining_seconds = divmod(time_difference.seconds, 3600)
remaining_minutes = remaining_seconds // 60

# Calculate percentage completion
total_seconds_in_event = (event_date - event_date.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
elapsed_seconds = (current_datetime - event_date.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
percentage_completion = (elapsed_seconds / total_seconds_in_event) * 100


print(f"Remaining time until the event: {remaining_days} days, {remaining_hours} hours, {remaining_minutes} minutes.")
print(f"Percentage completion of the event: {math.floor(percentage_completion)}%")
'''
Output - Remaining time until the event: 31 days, 9 hours, 0 minutes.

Percentage completion of the event: -3971%
'''


