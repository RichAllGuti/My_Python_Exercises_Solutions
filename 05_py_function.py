"""
Povided two strings, find the number of common characters between them.


"""
def common_character_in_string(string_one, string_two):
    #
    # Here we initialize two dictionaries to keep track of the count of each character in input parameters.
    count_string_one = {}
    count_string_two = {}

    # Here iterate over the dictionaries to count the characters and add them to correspondiente variables
    for char in string_one:
        count_string_one[char] = count_string_one.get(char, 0) + 1
    #
    for char in string_two:
        count_string_two[char] = count_string_one.get(char, 0) + 1
    
    # will track the number of common characters between both dictionaries
    match_char = 0

    # Here we going to iterate over the characters in string_one.
    for char in string_one:
        if char in  count_string_two and count_string_two[char] > 0:
            match_char += 1
            count_string_two[char] -=1

    return match_char

string_one = "Hello"
string_two = "good bye"

print(common_character_in_string(string_one, string_two))

