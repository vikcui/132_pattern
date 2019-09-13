# author: YANG CUI
"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.
Approach: Improved Brute Force
"""

def find132pattern(nums):
    """
    :param nums: input list of nums
    :return: True if there is a 132 pattern False Otherwise
    :time complexity: O(n^2)

    """
    if len(nums) < 3:
        return False
    i = 2 ** 32
    j = 0
    while j < len(nums) - 1:
        i = min(nums[j], i)
        k = j + 1
        while k < len(nums):
            if i < nums[k] < nums[j]:
                return True
            else:
                k += 1
        j += 1
    return False

print(find132pattern([-1,3,2,0]))