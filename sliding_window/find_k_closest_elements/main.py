class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import heapq
        diffs = [(abs(num - x), num) for num in arr]
        closest_pairs = heapq.nsmallest(k, diffs)
        result = [val for diff, val in closest_pairs]
        return sorted(result)
