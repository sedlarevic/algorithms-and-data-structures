class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count1 = {}
        count2 = {}
        for char in s:
            count1[char] = count1.get(char,0)+1
        for char in t:
            if char not in count1:
                return False
            count2[char] = count2.get(char,0)+1
        if count1==count2:
            return True
        return False

