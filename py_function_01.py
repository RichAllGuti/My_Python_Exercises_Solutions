# With a given string please verify if it is palindrome.
def is_palindrome(p_string):
    if p_string == p_string[::-1]:
        return f"{True} Is a palindrom."
    else:
        return f"{False} Is not a palindrom"

print(is_palindrome('oso'))