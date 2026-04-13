class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for k in freq:
            if freq[k] > len(nums)//2:
                return k
        
# Boyer-Moore Majority Voting Algorithm

class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate =-1
        votes = 0
        for n in nums:
            if votes == 0:
                votes = 1
                candidate = n
            else:
                if candidate == n:
                    votes += 1
                else:
                    votes -= 1
        return candidate
