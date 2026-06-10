class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if k == 0:
            return False

        distinctNums = set(nums)
        if len(distinctNums) == len(nums):
            return False
        
        for startWindow in range(len(nums) - 1):
            for endWindow in range(startWindow + 1, min(startWindow + k + 1,len(nums))):
                if nums[startWindow] == nums[endWindow]:
                    return True
            
        return False
