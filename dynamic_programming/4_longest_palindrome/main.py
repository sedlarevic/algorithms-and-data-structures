class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        count = 0
        has_odd = False

        for c in freq:
            # ako je freq[c] = 5 onda // 2 == 2
            count += (freq[c] // 2) * 2
            if freq[c] % 2 == 1:
                has_odd = True
        
        return count+1 if has_odd else count
 
        
