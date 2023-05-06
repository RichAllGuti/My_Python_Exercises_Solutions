"""
Given an integer number determine if all digits of it are even. 
"""
def are_all_digits_even(n: int) -> bool:
    """
    Determines whether all digits of a given integer are even.

    Args:
    - n (int): The integer to check.

    Returns:
    - bool: True if all digits of the integer are even, False otherwise.
    """
    digits = [int(digit) for digit in str(n)]
    return all(digit % 2 == 0 for digit in digits)


input_i = 84262688
input_i = 84262687

print(are_all_digits_even(input_i))