class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(path, startOpen, startClosed,rule):
            if len(path) == n*2:
                res.append(path)
                return
            
            if startOpen < n:
                backtrack(path + "(",startOpen+1,startClosed,rule+1)
            if startClosed < n and rule>0:
                backtrack(path + ")",startOpen,startClosed+1,rule-1)


        backtrack("",0,0,0)

        return res
