"""
INPUT
Given an integer array nums -> nums = [-1,0,1,2,-1,-4]
    -integer list, with positive and negative numbers.
    -length of list >= 3 and less than 3000
    - value of ints -10k -> 10k

OUTPUT
Return all the triplets [nums[i], nums[j], nums[k]] -> such that i != j, i != k, and j != k and nums[i] + nums[j] + nums[k] == 0
Notice that the solution set must not contain duplicate triplets.
    -return value should be a list
    -if there is not existing triplet return empty list []
    -other than that, return list of triplets where i j and k are distinct (remember the combination), and nums[i]+nums[j]+nums[k] == 0
        - what is distinct?
            - -1 + 0 + 1 vs 0 + 1 + -1
            - if the sum is 0, i can sort the combination and see if it exists in the return list of triplets
        - sum nums[i]+nums[j]+nums[k] == 0

EXPLAINING TO MYSELF
    Array of nums is given as an input, the output should be an array of arrays of triplets nums, where i!=j, j!=k, i!=k and nums[i]+nums[j]+nums[k] == 0.

ITERATING


EXAMPLE 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.
"""
class Solution(object):
    def threeSumSPOR(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):                   
                    if nums[i]+nums[j]+nums[k] == 0:
                        sorted_comb = sorted([nums[i],nums[j],nums[k]])
                        if sorted_comb not in res:
                            res.append(sorted_comb)
        return res
        
    def threeSum(self, nums):
        nums.sort()  # Sorting is required for Two Pointers
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Optimization 1: If the current number is positive, we can stop.
            # Since the array is sorted, we can't sum to 0 using only positive numbers.
            if nums[i] > 0:
                break
                
            # Optimization 2: Skip duplicate 'i' values to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Use Two Pointers for the remaining two numbers
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Sum is too small, move left pointer to increase it
                elif total > 0:
                    right -= 1 # Sum is too big, move right pointer to decrease it
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Optimization 3: Skip duplicates for 'left' and 'right'
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return result
