class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left, right = max(nums), sum(nums)

        def getNumSubarr(val):
            s = 0
            numSubarr = 1
            for num in nums:
                if s + num <= val:
                    s += num
                else:
                    numSubarr += 1
                    s = num                    
            return numSubarr

        while left < right:
            mid = left + (right - left) // 2
            if getNumSubarr(mid) <= k:
                right = mid
            else:
                left = mid + 1
        
        return left
