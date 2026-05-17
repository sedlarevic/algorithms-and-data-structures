class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def solveByString(x):
            #solution with reverse
            
            string = str(x)
            reverse = string[::1]

            #solution with reading half of characters

            # length = len(string)
            # i = 0
            # while i<length//2:
            #     if string[i] != string[length-i-1]:
            #         return False
            #     i += 1
            # return True

            return string == reverse

        # COOL SOLUTION
        if x < 0:
            return False
        temp = x
        summation = 0
        while temp>0:
            summation *= 10
            summation += temp%10
            temp //= 10
        return x==summation
        
