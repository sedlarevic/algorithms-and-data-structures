# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(path,target,curr):
            if not curr:
                return

            target -= curr.val
            path.append(curr.val)

            if target == 0 and not curr.left and not curr.right:
                res.append(path[:])
            else:
                backtrack(path,target,curr.left)
                backtrack(path,target,curr.right)

            path.pop()

        backtrack([],targetSum,root)
        return res
