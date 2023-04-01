"""
Check if the given string is a correct time representation of the 24-hour clock.

The function must retunr a True or False.
"""

def is_valid_time(time):
    
    # Split the time input in to hours and time .
    h, m = time.split(':')

    # Validate if the hours and minutes are validate integers
    if not h.isdigit() or not m.isdigit():
        #
        return False
    
    # Converting to integer the hours and minutes
    h = int(h)
    m = int(m)

    # Validate if hours and minutes are in the correct rage of time.
    if h < 0 or h > 23 or m < 0 or m > 59:
        return False
    
    #
    return True
    

input_time = "13:58"
input_time = "25:51"
input_time = "02:76"

print(is_valid_time(input_time))

