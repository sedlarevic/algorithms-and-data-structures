class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            position = (left + right) // 2
            if target == nums[position]:
                return position
            elif target < nums[position]:
                right = position - 1
            elif target > nums[position]:
                left = position + 1
        return -1
