"""

Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
Note: Sequence containing only one element is also considered to be strictly increasing.


The intention to this practice is to clarify each step of the code to help in the understanding what I do.

"""
def is_possible_strictly_increasing_sequence(sequence):
    #
    # define a flag it will be used to track if we have already removed an element
    removed = False
    
    # The for loop iterates over the indices of the sequence starting from index 1 
    for i in range(1, len(sequence)):
        
        # Validate the current element if less than or equal to the previous element, so we need to remove an element from the sequence to make it increasing
        if sequence[i] <= sequence[i-1]:

            # If already removed an element, we can't remove another element, so we return False.
            if removed:
                return False
            """
            If we haven't removed an element yet and the current element is greater than the element before the previous element, 
            then we can remove the previous element to make the sequence increasing. 
            So, we update the previous element to be equal to the current element. 
            """
            if i == 1 or sequence[i] > sequence[i-2]:
                sequence[i-1] = sequence[i]

            # If the previous if not match, then we need to remove the current element to make the sequence increasing and we update the current element to be equal to the previous element.
            else:
                sequence[i] = sequence[i-1]
            
            # We set the removed flag to True to indicate that we have removed an element.
            removed = True
    #        
    return True




sequence = [1, 2, 2, 3, 4] # True
sequence = [1, 3, 2, 5, 4] # False
print(is_possible_strictly_increasing_sequence(sequence))
