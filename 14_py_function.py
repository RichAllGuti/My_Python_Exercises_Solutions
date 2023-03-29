"""
Given string:
    Find the leftmost digit that occurs.

The function must return the digit.
"""
def find_first_left_digit(input_string):

    # Initialize a set with all possibles digits.
    digits = set("0123456789")

    # Just iterate each element of the input_string. 
    for char in input_string:

        # Validate if the value os char is in the set.
        if char in digits:
            return char
    
    # Using None is the input string no have digits.
    return None

#i_string = "Hi this is 123"
#i_string = "Hi this is None"
i_string = "Hi this is 450"

print(find_first_left_digit(i_string))

