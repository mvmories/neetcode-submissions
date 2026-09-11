from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    nums_sum = 0
    for num in nums:
        nums_sum += num
    return nums_sum 

def get_min(nums: List[int]) -> int:
    nums_min = nums[0]
    for num in nums:
        if num < nums_min:
            nums_min = num
    return nums_min

def get_max(nums: List[int]) -> int:
    nums_max = nums[0]
    for num in nums:
        if num > nums_max:
            nums_max = num 
    return nums_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
