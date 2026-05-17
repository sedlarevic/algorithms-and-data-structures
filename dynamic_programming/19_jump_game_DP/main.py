class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        right = 0
        last = len(nums)-1
        for i in range(len(nums)):
            if i > right:
                return False
            if nums[i] + i > right:
                right = nums[i] + i
            if last < right:
                return True
        return True

