# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tail = head
        passed = []
        while tail:
            if not tail:
                return False
            if tail in passed:
                return True
            else:
                passed.append(tail)
                tail = tail.next
        return False


        
