# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        l_tail, r_tail = left, right
        while head:
            if head.val < x:
                l_tail.next = head
                l_tail = l_tail.next
            else:
                r_tail.next = head
                r_tail = r_tail.next
            head = head.next
            
        l_tail.next = right.next
        r_tail.next = None

        return left.next