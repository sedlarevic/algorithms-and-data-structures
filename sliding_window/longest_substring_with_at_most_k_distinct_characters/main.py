'''
Description

Given a string s and an integer k,
return the length of the longest substring of s,
that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
'''

class Solution(object):
    def FindLongestSubstringAtMostKChars(self, s: str,  k: int) -> int:
        distinctChars = {}
        startWindow = 0
        maxLenSize = 0
        for endWindow in range(len(s)):

            distinctChars[s[endWindow]] = distinctChars.get(s[endWindow], 0) + 1

            while len(distinctChars) > k:
                distinctChars[s[startWindow]] -= 1
                if distinctChars[s[startWindow]] == 0:
                    distinctChars.pop(s[startWindow])
                startWindow += 1
            
            maxLenSize = max(maxLenSize, endWindow - startWindow + 1)

        return maxLenSize

