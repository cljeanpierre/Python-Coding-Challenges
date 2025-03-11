#HackerRank (Basic)

'''
Challenge 
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example: 07:05:45PM

'''

#Time Conversion


def timeConversion(s):
    period = s[-2:]  #returns last two characters- AM or PM
    hour = int(s[:2]) #extract the hour and convert it to an integer - 07 becomes 7 
    minutes_seconds = s[2:-2] #extract the :MM:SS part - :05:45
    
    if period == "AM":
        if hour == 12:  #12AM become 0
            hour = 0
    else: #meaning it's PM
        if hour != 12:
            hour += 12 #Add 12 (except for 12PM)
            
    military_time = str(hour).zfill(2) + minutes_seconds #zfill ensures formatting to always get 2 digits
    return military_time


print(timeConversion("12:00:00AM"))  # Expected output: "00:00:00"
print(timeConversion("01:05:45AM"))  # Expected output: "01:05:45"
print(timeConversion("11:59:59AM"))  # Expected output: "11:59:59"
print(timeConversion("12:00:00PM"))  # Expected output: "12:00:00"
print(timeConversion("01:00:00PM"))  # Expected output: "13:00:00"
print(timeConversion("07:05:45PM"))  # Expected output: "19:05:45"
print(timeConversion("11:59:59PM"))  # Expected output: "23:59:59"
