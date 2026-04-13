class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for char in s:
            if char in brackets:
                if stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True

