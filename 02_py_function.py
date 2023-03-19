"""
A n-interesting polygon is just a square with a side of length.
Find the area of a polygon for a given 'n'.
"""
#
def calculate_polygon_area(n):
    #
    # validate if n is defferent of number 1, return 1 if it True
    if n == 1:
        return 1
    else:   # return the result of n-1 exponentiation to 2 and n exponentiation to 2 
        return (n-1)**2 + n**2
#
print(calculate_polygon_area(4))