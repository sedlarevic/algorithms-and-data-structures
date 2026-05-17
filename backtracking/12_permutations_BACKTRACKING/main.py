class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(path):
            # Base case -> All numbers in nums
            # Constraints -> When the path length is the same as length of nums
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                # Choices -> Can't use the same number more than once in our path
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                # Backtracking Step -> Pop the last number added
                path.pop()
            
        
        backtrack([])
        return res

