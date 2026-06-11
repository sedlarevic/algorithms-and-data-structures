class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxAvg = -float('inf')
        startWindow = 0
        cur = 0
        n = len(nums)
        if n == 1:
            return float(nums[0])

        for endWindow in range(0, n):
            cur += nums[endWindow]
            subarrLen = endWindow - startWindow + 1
            while subarrLen > k:
                cur -= nums[startWindow]
                startWindow += 1
                subarrLen = endWindow - startWindow + 1
            if subarrLen == k:
                maxAvg = max(maxAvg, float(cur) / float(endWindow - startWindow + 1))
            
        return maxAvg
