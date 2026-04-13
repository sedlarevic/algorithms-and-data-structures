class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        stack = []
        
        for num in nums:
            if num in stack:
                stack.remove(num)
            else:
                stack.append(num)

        return stack[0]

