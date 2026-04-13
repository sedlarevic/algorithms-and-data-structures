class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                profit = prices[j]-prices[i]
                if profit > max:
                    max = profit
        return max

class SolutionBetter(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        max = 0
        for i in range(1,len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                profit = prices[i]-min
                if profit > max:
                    max = profit
        return max
