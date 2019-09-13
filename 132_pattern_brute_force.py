# author: YANG CUI
"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.
Approach: Brute Force
"""

def find132pattern(nums):
    """
    :param nums: input list of nums
    :return: True if there is a 132 pattern False Otherwise
    :time complexity: O(n^3)
    """
    if len(nums) < 3:
        return False
    firstIndex = 0
    while firstIndex < len(nums) - 2:
        secondIndex = firstIndex + 1
        while secondIndex < len(nums) - 1:
            thirdIndex = secondIndex + 1
            while thirdIndex < len(nums):
                if nums[firstIndex] < nums[thirdIndex] < nums[secondIndex]:
                    return True
                else:
                    thirdIndex += 1
            secondIndex += 1
        firstIndex += 1
    return False

print(find132pattern([1, 2, 3, 4]))