class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs or any(not s for s in strs):
            return ""

        prefix = ""
        i = 0
        minLength = len(min(strs, key=len))

        while i < minLength:
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                prefix += char
                i += 1
            else:
                break
        
        return prefix

