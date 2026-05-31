class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        minLength = float('inf')
        curSum = 0
        windowStart = 0

        for windowEnd in range(len(nums)):
            curSum += nums[windowEnd]
            while curSum >= target:
                minLength = min(minLength, windowEnd-windowStart + 1)
                curSum -= nums[windowStart]
                windowStart += 1

        if minLength == float('inf'):
            minLength = 0

        return minLength
