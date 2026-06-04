class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        startWindow = 0
        longestSubstringLength = 0
        chars = []
        for endWindow in range(len(s)):
            if s[endWindow] in chars:
                while s[endWindow] in chars:
                    del chars[0]
                    startWindow += 1
            else:
                longestSubstringLength = max(longestSubstringLength, endWindow - startWindow + 1)
            chars.append(s[endWindow])
        return longestSubstringLength
