#
# With a given string please verify if it is palindrome.
#
def is_palindrome(p_string):
    #
    #Validating whether the p_string is a palindrome using python slice notation in the [::-1] to reverse the string for compares it with the p_string input.
    if p_string == p_string[::-1]:
        return f"{True} Is a palindrom."
    else:
        return f"{False} Is not a palindrom"

print(is_palindrome('oso'))
