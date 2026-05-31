209. Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum/description/


int WindowStart
int MinWindowSize
int CurSum

for int WindowEnd in array...
    CurSum += array[WindowEnd]
    while CurSum >= TargetSum:
        MinWindowSize = min(MinWindowSize, WindowEnd - WindowStart + 1
        CurSum -= array[WindowStart]
        WindowStart++

return MinWindowSize

