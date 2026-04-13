class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distinct = set(nums)
        if len(distinct) == len(nums):
            return False
        return True
