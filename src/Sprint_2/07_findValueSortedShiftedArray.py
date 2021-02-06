"""

You are given a sorted array in ascending order that is rotated at some unknown pivot (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]) and a target value.

Write a function that returns the target value's index. If the target value is not present in the array, return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

[execution time limit] 4 seconds (py3)

[input] array.integer nums

[input] integer target

[output] integer
"""
def findValueSortedShiftedArray(nums, target):
    # case 1 - target not present
    # set result to -1
    result = -1

    # iterate with enumerate to find index and value
    for index, value in enumerate(nums):
        # compare value to target
        if value == target:
            # set result to index
            result = index
            # return result index
            return result
    # return case 1 result -1
    return result

    
#Example 1:
#Input: 
nums = [4,5,6,7,0,1,2] 
target = 0
print(findValueSortedShiftedArray(nums, target))
#Output: 4

#Example 2:
#Input: 
nums = [4,5,6,7,0,1,2] 
target = 3
print(findValueSortedShiftedArray(nums, target))
#Output: -1



"""
# case 1 - target not present
# set result to -1
# iterate with enumerate to find index and value
    # compare value to target
        # set result to index
        # return result index
# return case 1 result -1
"""
    
