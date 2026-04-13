class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(index, path):
            # Base case - backtracking algorithm has gotten to the leaf of a tree
            if index == len(nums):
                res.append(path[:])
                return
            
            # Decision 1 - Include a number to the path   
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()

            # Decision 2 - Not include a number to the path
            backtrack(index+1,path)

        backtrack(0,[])
        return res
