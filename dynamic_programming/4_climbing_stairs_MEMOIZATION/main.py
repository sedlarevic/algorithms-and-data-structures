class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.climb(n)

    def climb(self, n, memo={}):
        if n in memo:
            return memo[n]
        if n==0:
            return 1
        if n<0:
            return 0
        
        memo[n] = self.climb(n-1)+self.climb(n-2)
        return memo[n]
