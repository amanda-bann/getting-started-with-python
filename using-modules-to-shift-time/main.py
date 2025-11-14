# Import the datetime library
import datetime

# Write the variable that stores the current time
current_time = datetime.datetime.now()

# Time
print(current_time.strftime("%I:%M %p"))

# Date
print(current_time.strftime("%m/%d/%y"))
print(current_time.strftime("%B %d, %Y"))

# Date and Time
print(current_time.strftime("%B %d, %Y %I:%M: %p"))

