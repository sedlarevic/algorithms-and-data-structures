class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        def isCharSmallerOrEqualsThanTarget(index, target):
            return letters[index] <= target

        left, right = 0, len(letters)

        while left < right:
            mid = left + (right - left) // 2
            if isCharSmallerOrEqualsThanTarget(mid, target):
                left = mid + 1
            else:
                right = mid
        if right == len(letters):
            return letters[0]
        else:
            return letters[right]
