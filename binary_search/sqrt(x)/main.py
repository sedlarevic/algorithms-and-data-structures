class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def condition(value, x):
            return value * value <= x

        if x == 0:
            return 0
        if x == 1 or x == 2:
            return 1

        left, right = 0, x
        mid = left + (right - left) // 2
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid, x):
                left = mid + 1
            else:
                right = mid

        return right - 1
