class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Creating an array size of amount. All elements of an array are set to infinity, except the first element.
        res = [float('inf')] * (amount+1)
        res[0] = 0
        # Nested loops. Outer loop iterates over the array of coins. Inner loop goes from value of coin (from outer loop) up to the amount. 
        for coin in coins:
            for current_amount in range(coin, amount+1):
                # Inside the loop, we update the current position in res array. The new value is minimum of a current value, or value of current index minus coin value plus 1. This insures that we store the fewest number of coins to make the amount.
                res[current_amount] = min(res[current_amount], res[current_amount - coin] + 1)
        # We check if the last element is still infinity, if it is, return -1, if not, return res[amount]
        return res[amount] if res[amount] != float('inf') else -1
