class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def isSmallerThanTarget(index, target):
            return nums[index] < target

        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif isSmallerThanTarget(mid, target):
                left = mid + 1
            else:
                right = mid

        if nums[mid] > target:
            return mid
        else:
            return mid + 1
