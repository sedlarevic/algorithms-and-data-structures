# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        
        def resolve(leftHalf,rightHalf):
            if not leftHalf and not rightHalf:
                return True
            if not leftHalf or not rightHalf or leftHalf.val!=rightHalf.val:
                return False

            return resolve(leftHalf.left,rightHalf.right) and resolve(leftHalf.right,rightHalf.left)

        return resolve(root.left,root.right)
