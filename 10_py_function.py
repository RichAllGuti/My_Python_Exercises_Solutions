"""
Given an integer number determine if all digits of it are even. 
"""
def is_even_digit(integer_input):

    # Just convert the integer input, to access individual digits
    digits_string = str(integer_input)

    # Just iterate through each character in the string
    for digits in digits_string:

        #Check if the digit is old
        if int(digits) % 2 == 1:
            
            # if the digit is odd we must return False "not all digits are even"
            return False
    
    #
    return True

input_i = 84262688
input_i = 84262687

print(is_even_digit(input_i))
