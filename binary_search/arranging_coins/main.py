class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        def condition(value):
            return value*(value+1) // 2 <= n

        if n == 1:
            return 1

        left, right = 0, n

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
        
        return right - 1

