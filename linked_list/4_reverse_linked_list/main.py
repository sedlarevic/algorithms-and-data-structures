# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr=nxt
        return prev

        """
        1->2->3->4->5->N
        N<-1<-2<-3<-4<-5
        help = 2
        2.next = 1
        help = 3 
        3.next = 2
        help = 4 
        4.next = 3
        help = 5
        5.next = 4
        help = None
        1.next = None
        """


