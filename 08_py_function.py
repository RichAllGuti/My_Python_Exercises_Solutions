"""
Provided an array of integers, find the maximal absolute difference between any two of its adjacent elements.

The function must return the number.
"""
def max_absolute_difference_between(number_array):

    # This variable will keep track of the maximum difference between any two adjacent elements in the array.
    maximal_difference = 0

    # Iterate over the array from the first element to the second-to-last element, using the range function.
    for i in range(len(number_array) - 1):
        diff = abs(number_array[i] - number_array[i+1])
        if diff > maximal_difference:
            maximal_difference = diff
    
    #
    return maximal_difference

inputArray = [2, 4, 1, 9, 7]
print(max_absolute_difference_between(inputArray))

