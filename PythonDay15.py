# Time-of-day greeting program in Python
# This program will greet the user based on the time of day

import datetime
current_time = datetime.datetime.now()  # Get the current time
hour = current_time.hour
if hour> 5 and hour < 12:
    print("Good morning!")
elif hour > 12 and hour < 18:
    print("Good afternoon!")
elif hour > 18 and hour < 21:
    print("Good evening!")
else:
    print("Good night!")



















