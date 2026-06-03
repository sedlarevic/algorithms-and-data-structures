# Kadane's Algorithm
#https://www.youtube.com/watch?v=NUWAXbSlsws
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum

