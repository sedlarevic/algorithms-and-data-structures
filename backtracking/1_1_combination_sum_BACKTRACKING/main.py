class Solution(object):
    """
    INPUT:
        - Given an array of distinct integers candidates and a target integer target
        - List of candidates is sorted.
    OUTPUT:
        - Return a list of all unique combinations of candidates where the chosen numbers sum to target.

        - You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. 
        - Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    EXPLANATION:
        - As an input, the method gets a list of candidates, and an integer, target. 
        - Returned value should be list of lists, of all possible distinct combinations of ways to sum the candidates to get the target.
        - Combinations should be unique, by frequency of a chosen number.
    
    RULES:
        - Unique combinations by frequency of numbers, so we are looking at values, not indexes
        - Same index (value) can be chosen unlimited number of times.
        - Any order return of combinations
    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, target, path):
            if target == 0:
                res.append(path[:])
                return
    
            if target < 0:
                return

            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,target-candidates[i],path)
                path.pop()
            
        backtrack(0,target,[])
        return res
