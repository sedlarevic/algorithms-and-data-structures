class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        correct_array_of_nums = range(0,len(nums)+1,1)
        sum1 = sum(nums)
        sum2 = sum(correct_array_of_nums)
        # Moze i preko Gausove sume!
        n = len(nums)+1
        sum2 = n*(n-1)/2
        return sum2-sum1
