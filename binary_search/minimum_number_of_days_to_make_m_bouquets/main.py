class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        """
        PARAMETERS:
        array -> bloomDay where bloomDay[i] is the day where the i-th flower will bloom and can be used in exactly one bouquet
        m -> amount of bouquets that should be made
        k -> k adjacent flowers needed to make a specific bouquet
        RESULT:
        result -> minimum number days needed to make m bouquets, that are made of k adjacent flowers. if not posible, return -1
        """
        if len(bloomDay) < m * k:
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        
        def numOfBouquets(daysPassed):
            bouquets = 0
            i = 0
            flowersLeft = k
            # A little bit more readable:
            # flowers = 0
            # for day in bloomDay:
            #     if day <= daysPassed:
            #         flowers += 1
            #         if flowers == k:
            #             bouquets += 1
            #             flowers = 0
            #     else:
            #         flowers = 0
            while i < len(bloomDay):
                if bloomDay[i] <= daysPassed:                       
                    if flowersLeft > 0:
                       flowersLeft -= 1
                    if flowersLeft == 0:
                       flowersLeft = k
                       bouquets += 1
                else:
                    flowersLeft = k
                i += 1     
        
            return bouquets

        while left < right:
            mid = left + (right - left) // 2
            if numOfBouquets(mid) < m:
                left = mid + 1
            else:
                right = mid
        return right
        
