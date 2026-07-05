1. O(1) Management (Optimized Sliding Window):
  Usage: When you need to find a continuous subarray or substring that contains a specific required mix of elements.
  Giveaway: You are writing a Sliding Window, but inside the window, you are running a for loop to check a HashMap or frequency array to see if the window is valid. (Optimize this by tracking a single 'matched' integer instead).
  Practice Problems:
    Minimum Window Substring (LeetCode 76)
    Permutation in String (LeetCode 567)
    Find All Anagrams in a String (LeetCode 438)
2. Knapsack DP:
  Usage: You are given a pool of distinct items. Each item has a cost (weight) and a reward (value). You have a strict limit (capacity).
  Giveaway: You are making a binary "take it or leave it" choice for every single item, and there is a hard limit you cannot cross. (For further optimization, collapse the 2D matrix into a 1D array and manipulate the loop direction).
  Problems:
    Partition Equal Subset Sum (LeetCode 416) - 0/1 Knapsack
    Coin Change (LeetCode 322) - Unbounded Knapsack
    Target Sum (LeetCode 494)
3. Longest Increasing Subsequence (LIS):
  Usage: When you need to find the longest sequence of items that follow a sorting rule (asc/desc), but the items don't have to be continuous (next to each other).
  Giveaway: You realize the O(N2) DP is too slow. (Use Binary Search on the array to overwrite elements and "lower the barrier" for future numbers in O(N log N) time).
  Problems:
    Longest Increasing Subsequence (LeetCode 300)
    Largest Divisible Subset (LeetCode 368)
    Minimum Number of Removals to Make Mountain Array (LeetCode 1671)
4. 2D-to-1D Compression:
  Usage: When you are looking for rectangular areas, perimeters, or counts of submatrices within a 2D grid.
  Giveaway: The problem forces a rigid 2D geometric shape (a perfect rectangle) across a grid of binary integers (0s and 1s, or usable vs. unusable, or X and O chars). (Condense rows horizontally, then use a Monotonic Stack vertically).
  Problems:
    Largest Rectangle in Histogram (LeetCode 84)
    Maximal Rectangle (LeetCode 85)
    Count Submatrices With All Ones (LeetCode 1504)
5. Geometric Dimensions DP:
  Usage: When you are given pairs of coordinates, dimensions, or intervals, and you need to nest them, connect them, or fit them without crossing.
  Giveaway: The input is an array of 2D pairs: [[w, h], [w, h], ...], and the problem restricts you from using items that overlap or cross in 2D space. (Sort the first dimension ascending, sort the second dimension descending as a tie-breaker, then run 1D LIS).
  Problems:
    Russian Doll Envelopes (LeetCode 354)
    Maximum Length of Pair Chain (LeetCode 646)
    Building Bridges (Classic GeeksForGeeks / CP problem)
6. Interval DP:
  Usage: When removing/bursting/merging/collapsing an element causes the remaining elements to collapse and become new neighbours.
  Giveaway: The problem asks for a max/min score, and the score depends on the elements directly adjacent to the one you are interacting with. The constraints are usually N <= 500. (Ask what happens last to build an unbreakable wall, isolating the subproblems).
  Practice Problems:
    Burst Balloons (LeetCode 312)
    Minimum Cost to Merge Stones (LeetCode 1000)
    Minimum Score Triangulation of Polygon (LeetCode 1039)
7. Digit DP:
  Usage: You are asked to count how many numbers within a massive range [L, R] have a specific property (e.g., digit sum is prime, contains no repeated digits).
  Giveaway: The upper limit R is very large (like 1018), meaning a standard for loop will instantly give a Time Limit Exceeded (TLE) error. You must build the numbers digit-by-digit as strings using DFS and a tight boolean constraint.
  Practice Problems:
    Number of Digit One (LeetCode 233)
    Count of Integers (LeetCode 2719)
    Numbers At Most N Given Digit Set (LeetCode 902).

Word break je jako tezak vrati se na njega.

https://leetcode.com/problems/word-break/
https://leetcode.com/problems/coin-change/description/
https://leetcode.com/problems/jump-game/description/
https://leetcode.com/problems/climbing-stairs/description/
https://leetcode.com/problems/decode-ways/description/
https://leetcode.com/problems/unique-paths/description/
https://leetcode.com/problems/longest-increasing-subsequence/description/
https://leetcode.com/problems/maximum-subarray/description/
