"""
With a provided string, your task is to replace each of its characters by the next one in the English alphabet; i.e. 
replace 'a' with 'b', replace 'b' with c, etc (z would be replaced by a).
"""
def alphabetic_char_replace(input_string):

    # simple initialization of empty string to store the result
    result = ""
    
    # Iterate through each character in the input string
    for char in input_string:
    
        # validate if the character is 'z'
        if char == 'z':
            # if it is, append 'a' to the result string
            result += 'a'
        else:
            """
             Otherwise, get the ASCII code of the character and add 1 to it
             then use the chr() function to convert the new ASCII code to its corresponding character
             and append it to the result string 
             """
            result += chr(ord(char) + 1)
    
    
    return result


i_string = "abcdifgmnlop"

print(alphabetic_char_replace(i_string))
