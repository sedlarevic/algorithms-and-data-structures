class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp becomes
        # [False,False,False... for the length of target string + 1]
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and dp[i-len(word)]:
                    if s[i-len(word):i] == word:
                        dp[i] = True

        return dp[len(s)]
