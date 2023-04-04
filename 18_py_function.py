"""
Consider integer numbers from 0 to 'n - 1' written down along the circle in such a way that the distance
between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Provided a n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

"""
def calculate_radially_opposite_position(n_number, first_number):

    # Calculate the number if integers between 0 and n_number - 1 that are equally spaced along the circle.
    num_ints = n_number // 2

    #Calculate the position of the oppositenumber relative to the first number.
    opposite_position = (first_number + num_ints) % n_number

    #
    return opposite_position

print(calculate_radially_opposite_position(10,2))
