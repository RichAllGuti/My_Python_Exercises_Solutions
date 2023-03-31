""" 
Let's define digit degree of some positive integer as the number of times we need to replace this number with:
The sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

"""
def define_digit_degree(input_number):
    
    d_degree = 0

    # Iterate until input number is a one-digit number.
    while input_number >= 10:

        #
        digit_sum = 0

        # Iterate over the digits in input number
        for digit in str(input_number):

            # Add each digit to the sume
            digit_sum += int(digit)
        
        # Replace the input number with the sum of it digits
        input_number = digit_sum

        # Increment the digit degree fot the while iteration.
        d_degree += 1

    return d_degree
    
number = 9
number = 100
number = 91

print(define_digit_degree(number))