from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    # [1,2,3] 
    # [4,5,6]
    # [7,8,9]   len(row) = 4 len (col) = 3

    # check for negative numbers:
    if r < 0 or c < 0:
        return False

    #check lenght of grid row
    # if smaller than r-1, return False (out of bounds)
    if len(grid) - 1 < r:
        return False
    
    # Assuming 2d Grid, check num of cols
    #if num of cols < c - 1 (out of bounds)
    if len(grid[0]) - 1 < c:
        return False
    
    return True


# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))
