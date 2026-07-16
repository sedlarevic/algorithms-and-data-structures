# Easy - Brute force

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([n*n for n in nums])

# Two Pointers

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        res = [0] * n
        for pos in range(len(nums) - 1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            if left_square > right_square:
                res[pos] = left_square
                left += 1
            else:
                res[pos] = right_square
                right -= 1

        return res
