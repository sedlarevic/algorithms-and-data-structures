class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        left, right = 1, sum(weights)

        def calculateDays(capacity):
            if capacity < max(weights):
                return float('inf')
            daysShipping = 1
            curWeight = 0
    
            for weight in weights:
                if curWeight + weight <= capacity:
                    curWeight += weight
                else:
                    daysShipping += 1
                    curWeight = weight
                    
            return daysShipping
            
        def compareDays(capacity):
            return calculateDays(capacity) <= days

        while left < right:
            mid = left + (right - left) // 2
            if compareDays(mid):
                right = mid
            else:
                left = mid + 1
        return right
