class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        left, right = 1, max(piles)

        def calculateHours(value):
            hrs = 0
            for pile in piles:
                hrs += (pile + value - 1) // value
            return hrs

        def compareHours(value):
            return calculateHours(value) <= h

        while left < right:
            mid = left + (right - left) // 2
            if compareHours(mid):
                right = mid
            else:
                left = mid + 1
        return left
