class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        res = []
        while i<=j:
            if abs(nums[i])>abs(nums[j]):
                res.append(nums[i]*nums[i])
                i += 1
            else:
                res.append(nums[j]*nums[j])
                j -= 1
        return res[::-1]
