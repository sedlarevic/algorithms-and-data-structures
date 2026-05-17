# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max = 0
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def traverse(root):
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            height = 1 + max(left,right)

            if left+right>self.max:
                self.max = left+right
            
            return height
   
            
        result = traverse(root)
        return self.max

