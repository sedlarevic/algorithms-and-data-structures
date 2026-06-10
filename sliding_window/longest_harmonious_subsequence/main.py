class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longestSeq = 0
        frequencies = {}
        for item in nums:
            frequencies[item] = frequencies.get(item, 0) + 1
        
        for frequency in frequencies:
            if frequency + 1 in frequencies:
                longestSeq = max(longestSeq, frequencies[frequency] + frequencies[frequency + 1])
    
        return longestSeq
