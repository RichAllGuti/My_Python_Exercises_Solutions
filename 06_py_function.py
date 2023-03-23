"""
Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not with True or False output.
"""
def perferct_ticket_number(ticket_number):
    
    # To manipulate the digits we need to conver the ticket number into string.
    ticket_number_string = str(ticket_number)

    # Find the midpoint of the string
    half = len(ticket_number_string)//2

    # Calculate the sume of the first half of the string
    first_half_sum = sum(int(digit) for digit in ticket_number_string[:half])

    # Calculate the sume of the second half of the string
    second_half_sum = sum(int(digit) for digit in ticket_number_string[half:])

    # Calculate the result to get the True or False answer, comparing the first and secon sum calculation and the len of the input string.
    result = first_half_sum == second_half_sum and len(ticket_number_string)%2==0

    return result

ticket = 1222
ticket = 12344321
print(perferct_ticket_number(ticket))

