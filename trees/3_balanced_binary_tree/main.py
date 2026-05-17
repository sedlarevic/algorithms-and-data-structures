# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def dfs(root):
            #base case je da li je root tree balansiran? Jeste, stoga se vraca da je njegov height 0 i vraca se True, zato sto je balansiran
            if not root:
                return [0,True]
            #depth first search za levi subtree i za desni
            left = dfs(root.left)
            right = dfs(root.right)
            #ovde proveravamo da li je root node balansiran
            #to radimo tako sto radimo apsolutnu vrednost od levog i desnog subtree-a.
            #takodje moramo da proverimo da li je levi i densi subtree od tog roota balansiran, jer ako nije onda je odmah false
            balanced = (left[1] and right[1] and abs(left[0] - right[0])<=1)
            #vracamo balanced, dakle true ili false, kao i visinu samog tree-a.
            return [1 + max(left[0],right[0]),balanced]
        return dfs(root)[1]


class Solution2(object):
    def isBalanced(self,root):
        
        def dfs(root):
            if not root:
                return [0,True]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[1] and right[1] and abs(left[0],right[0])<=1)

            return [1 + max(left[0],right[0]), balanced)
        return dfs(root)[1]
