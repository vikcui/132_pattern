# author: YANG CUI
"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.
Note: n will be less than 15,000.
Approach: Using stack
"""

def find132pattern(nums):
    """
    :param nums: input list of nums
    :return: True if there is a 132 pattern False Otherwise
    :time complexity: O(n^2)
    """
    if len(nums) < 3:
        return False
    stack_list = []
    min_i = [0] * len(nums)
    min_i[0] = nums[0]
    for i in range(1, len(nums)):
        min_i[i] = min(nums[i], min_i[i - 1])
    j = len(nums) - 1
    while j >= 0:
        if nums[j] > min_i[j]:
            if len(stack_list) != 0 and min_i[j] < stack_list[0] < nums[j]:
                return True
            elif len(stack_list) == 0 or stack_list[0] > nums[j]:
                stack_list.insert(0, nums[j])
            elif stack_list[0] <= min_i[j]:
                stack_list.__delitem__(0)
                j += 1
        j -= 1
    return False


# print(find132pattern([3,5,0,3,4]))