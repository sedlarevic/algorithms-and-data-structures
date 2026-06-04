class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        numSlices = 0
        currentStreak = 0
        # Check every consecutive triplet
        for i in range(2,len(nums)):
            # If the difference matches the previous difference
            if nums[i] - nums[i-1] == nums[i - 1] - nums[i - 2]:
                currentStreak += 1
                numSlices += currentStreak
            else:
                # The chain is broken, reset the streak
                currentStreak = 0
        return numSlices
