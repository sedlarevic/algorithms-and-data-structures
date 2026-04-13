class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_string = [char for char in s if char.isalnum()]
        for i in range(len(new_string)//2):
            if new_string[i] != new_string[len(new_string)-i-1]:
                return False
        return True
        
