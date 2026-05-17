# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#idemo od donje ka gornjoj, od najstarije ka najmladjoj

class Solution1(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left,right = 0, n
        while left < right:
            mid = (left+right)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid+1
        return left
            
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#idemo od donje ka gornjoj, od najstarije ka najmladjoj

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 0
        while i<=n:
            badVersion = isBadVersion(i)
            if badVersion:
                return i
            i+=1
            
        
# a sa binary searchom, brze

           

