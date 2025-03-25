# Get a number of second from user. Calculate hours, minutes, and seconds. 
# print(f"{5 // 2}") 2
# print(f"{5 % 2}") 1
# Enter your seconds: 504030303939
# That is 140008417 hour 45 minute and 39 second.

Total_second = int(input("Enter your seconds:"))
# Calculate hours
hours = Total_second // 3600
# Calculate remaining minutes
minutes = (Total_second // 60) % 60
# Calculate the remaing seconds
seconds = Total_second % 60
# Display the result
print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)