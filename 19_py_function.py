"""
Given a sorted array of integers 'a', your task is to determine which element of 'a'is closest to all other values of 'a'. In other words, find the element 'x' in 'a', which minimizes the following sum:
abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)

If there are several possible answers, output the smallest one.

"""
def closest_integer_to_all_other_values(integer_array):
    
    #
    input_len = len(integer_array)

    # Find the median of the array by taking the element at index.
    array_median = integer_array[input_len // 2]

    # Initialize the minimum sum to a large value
    minimum_sum = float('inf')
    
    result = None

    # Iterate over the length
    for i in range(input_len):

        # Calculate the sum of absolute differences between integer_array[i] and all other elements
        current_sum = 0

        # Iterate over the len to determine the update of the current sum.
        for j in range(input_len):

            # Update the current sume
            current_sum += abs(integer_array[j] -integer_array[i])
            
            # if current sum is smaller than the minimum sum, update the result.
            if current_sum < minimum_sum:
                minimum_sum = current_sum
                result = integer_array[i]

        # if there are multiple elements that minimize the sum, return the smallest one.
        if minimum_sum == current_sum:
            return min(result, array_median)
        else: # Otherwise, return the element that minimizes the sum
            return result

#
a = [2,4,7]
b = [6,8,9]
c = [2,3]
d = [5,5,5]

print(closest_integer_to_all_other_values(a))

print(closest_integer_to_all_other_values(b))

print(closest_integer_to_all_other_values(c))

print(closest_integer_to_all_other_values(d))
