"""
In python a correct variable names that consist only of English letters, digits and underscores and they can't start with a digit.
validate if the given string is a correct variable name.

The function must return a True or False.
"""
def validate_correct_variable(var_name):
    
    # Just validate if the first caracter of the input is not a digit
    if var_name[0].isdigit():
        return False

    #
    for char in var_name:

        # Validate if the character is correct
        if not char.isalnum() and char != '_':
            return False
    
    return True

name = "var_1__Int"
#name = "qq-q"
#name = "2w2"

print(validate_correct_variable(name))

#