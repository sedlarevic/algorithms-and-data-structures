class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        def calculateDigitAndCarry(digit,carry):
            nextDigit = int(digit)
            if carry:
                nextDigit += 1
            if nextDigit>1:
                carry=True
                nextDigit-=2
            else:
                carry=False
            return nextDigit,carry

        carry = False
        outputString = ""
        while a and b:
            digitA = a[-1]
            digitB = b[-1]
            result = int(digitA) + int(digitB)
            result, carry = calculateDigitAndCarry(result, carry)
            outputString += str(result)

            a = a[:-1]
            b = b[:-1]

        rest = ""

        while a:
            digit = a[-1]
            nextDigit, carry = calculateDigitAndCarry(digit, carry)
            rest += str(nextDigit)
            a = a[:-1]
        while b:
            digit = b[-1]
            nextDigit, carry = calculateDigitAndCarry(digit, carry)
            rest += str(nextDigit)
            b = b[:-1]

        outputString += rest

        if carry:
            outputString += '1'

        return outputString[::-1]
