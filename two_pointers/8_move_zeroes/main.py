class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        while i < length:
            if nums[i]==0:
                nums.append(nums[i])
                nums.pop(i)
                length -= 1
            else:
                i += 1
        
