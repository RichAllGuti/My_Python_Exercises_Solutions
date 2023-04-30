#
# With a given string please verify if it is palindrome.
#
def is_palindrome(p_string):
    """
    This function takes a string and returns True if it is a palindrome, False otherwise.
    """
    # Using python slice notation in the [::-1] to reverse the string for compares it with the p_string input.
    reversed_string = p_string[::-1]
    
    # Checking if the reversed string is equal to the original string
    if p_string == reversed_string:
        return True
    else:
        return False

# Example usage
print(is_palindrome('oso'))
