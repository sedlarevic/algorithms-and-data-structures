class SolutionBackToFront(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # MCMXCIV
        romanToIntDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        rules = {
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900,
        }

        def peek(s,currentIndex):
            return s[currentIndex-1]

        def construct(char1,char2):
            return char1+char2

        sum = 0
        i = len(s)-1
        while i>=0:
            subtractRuleApplied = False
            result = s[i]
            if result != "I" and i>0:
                nextChar = peek(s,i)
                peekValue = construct(nextChar,result)
                if peekValue in rules:
                    subtractRuleApplied = True
                    result = peekValue
            
            if subtractRuleApplied:
                sum += rules[result]
                i -= 2
            else:
                sum += romanToIntDict[result]
                i -= 1
    
        return sum            


class SolutionFrontToBack(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanToIntDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        rules = {
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900,
        }

        def peek(s,currentIndex):
            return s[currentIndex+1]

        def construct(char1,char2):
            return char1+char2

        sum = 0
        i = 0
        while i<len(s):
            subtractRuleApplied = False
            result = s[i]
            if i+1<len(s) and peek(s,i) != "I":
                peekChar = peek(s,i)
                peekValue = construct(result,peekChar)
                if peekValue in rules:
                    subtractRuleApplied = True
                    result = peekValue
            
            if subtractRuleApplied:
                sum += rules[result]
                i += 2
            else:
                sum += romanToIntDict[result]
                i += 1
    
        return sum            



