"""
As discussed in the last approach, once we've fixed a nums[i],nums[j]nums[i],nums[j] pair, we just need to determine a nums[k]nums[k] which falls in the range (nums[i],nums[j])(nums[i],nums[j]). Further, to maximize the likelihood of any arbitrary nums[k]nums[k] falling in this range, we need to try to keep this range as much as possible. But, in the last approach, we tried to work only on nums[i]nums[i]. But, it'll be a better choice, if we can somehow work out on nums[j]nums[j] as well.
To do so, we can look at the given numsnums array in the form of a graph, as shown below:

From the above graph, which consists of rising and falling slopes, we know, the best qualifiers to act as the nums[i],nums[j]nums[i],nums[j] pair, as discussed above, to maximize the range nums[i], nums[j]nums[i],nums[j], at any instant, while traversing the numsnums array, will be the points at the endpoints of a local rising slope. Thus, once we've found such points, we can traverse over the numsnums array to find a nums[k]nums[k] satisfying the given 132 criteria.
To find these points at the ends of a local rising slope, we can traverse over the given numsnums array. While traversing, we can keep a track of the minimum point found after the last peak(nums[s]nums[s]).
Now, whenever we encounter a falling slope, say, at index ii, we know, that nums[i-1]nums[i−1] was the endpoint of the last rising slope found. Thus, we can scan over the kk indices(k>i), to find a 132 pattern.
But, instead of traversing over numsnums to find a kk satisfying the 132 pattern for every such rising slope, we can store this range (nums[s], nums[i-1])(nums[s],nums[i−1])(acting as (nums[i], nums[j])(nums[i],nums[j])) in, say an intervalsintervals array.
While traversing over the numsnums array to check the rising/falling slopes, whenever we find any rising slope, we can keep adding the endpoint pairs to this intervalsintervals array. At the same time, we can also check if the current element falls in any of the ranges found so far. If so, this element satisfies the 132 criteria for that range.
If no such element is found till the end, we need to return a False value.
"""

def find132pattern(nums):
    """
    :param nums: input list
    :return: True if there is a 132 pattern False Otherwise
    :time : O(n^2)
    :space : O(n)
    """
    intervals = []
    i = 1
    s = 0
    while i < len(nums):
        if nums[i - 1] >= nums[i]:
            if s < i - 1:
                intervals.append([nums[s], nums[i - 1]])
            s = i
        for interval in intervals:
            if interval[0] < nums[i] < interval[1]:
                return True
        i += 1
    return False

print(find132pattern([3, 1, 4, 2]))