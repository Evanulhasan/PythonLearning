import time 

timeStamp = time.strftime("%H:%M:%S")
print(timeStamp)
hour = int(time.strftime('%H'))
if hour > 4 and hour < 12:
    print("Good Morning")
elif hour > 12 and hour <5:
    print("Good Afternoon")
else:
    print("Good Evening")














