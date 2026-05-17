class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitsToChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        res = []

        charsDigitsList = []
        
        for digit in digits:
            charsDigitsList.append(digitsToChars[digit])

        def backtrack(startCharsDigitsList, path):
            if len(path) == len(charsDigitsList):
                res.append(path[:])
                return
            i = startCharsDigitsList
            for j in range (0,len(charsDigitsList[i])):
                path.append(charsDigitsList[i][j])
                backtrack(i+1,path)
                path.pop()
                

        backtrack(0,[])
        for i in range(len(res)):
            res[i] = "".join(res[i])

        return res
