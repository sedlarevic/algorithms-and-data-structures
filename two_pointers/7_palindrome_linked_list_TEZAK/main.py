# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        tail = head

        listLength = 0
        while tail:
            listLength += 1
            tail = tail.next

        if listLength == 1:
            return True
        if listLength == 0:
            return False

        tail = head
        stack = []
        halfLength = listLength//2
        compareStart = halfLength + (listLength % 2)
        count = 0
        while tail:
            if count >= compareStart:
                if tail.val == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                if count < halfLength:
                    stack.append(tail.val)
            
            tail = tail.next
            count += 1

        return True

        
