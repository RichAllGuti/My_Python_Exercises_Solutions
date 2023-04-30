"""
Find the area of a polygon for a given 'n'.
"""
#
def calculate_polygon_area(n):
    """
    This function takes an integer 'n' and returns the area of an n-interesting polygon, where an n-interesting polygon
    is defined as a square with n layers of cells on each side.
    """
    if n == 1:
        return 1
    else:
        # Calculate the area by summing the area of the previous n-1 square layers and adding the area of the nth layer.
        return (n-1)**2 + n**2

# Example usage
print(calculate_polygon_area(4))
