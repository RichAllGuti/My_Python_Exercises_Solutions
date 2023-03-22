"""
By a provided array of strings, return another array with all of its longest strings and.

We will return an array with the maximum or the maximums tring if there are more than one with the same string length.

"""
def longest_strings(array_string):
    
    # Here we initialize an empty list to used to store the longest string. 
    l_string = []

    # Set the variable max_length to zero it will hold the number of the length longest string.
    max_length = 0

    # Here we will find the maximum string length in the array_string
    for s in array_string:
        max_length = max(max_length, len(s))

    # Here we append all strings with length equal to max_length to be the longest string 'l_String' list 
    for s in array_string:
        if len(s) == max_length:
            l_string.append(s)
    
    #
    return l_string

#inputArray = ["aba", "aa", "ad", "vcd", "aba"]
inputArray = ["hello", "hi", "day", "night", "alternatives"]

print(longest_strings(inputArray))



