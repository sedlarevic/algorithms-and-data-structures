class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        def divideAndSum(divisor, arrDividend):
            return sum([-(-num // divisor) for num in arrDividend ])
        
        def isLesserOrEqual(a, b):
            return a <= b

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2
            if isLesserOrEqual(divideAndSum(mid, nums), threshold):
                right = mid
            else:
                left = mid + 1
        return left
