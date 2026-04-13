# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def startCheck(root,subRoot):
            if root and subRoot and root.val!=subRoot.val:
                return False
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            return startCheck(root.left,subRoot.left) and startCheck(root.right,subRoot.right)

        if not root:
            return False

        if root.val == subRoot.val:
            if startCheck(root, subRoot):
                return True
        
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)

        return left or right
