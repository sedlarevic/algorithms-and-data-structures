class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def bitCount(n):
            count = 0
            while n:
                n = n & n - 1
                count += 1
            return count

        arr = []
        for i in range(0,n+1,1):
            arr.append(bitCount(i))

        return arr
        
