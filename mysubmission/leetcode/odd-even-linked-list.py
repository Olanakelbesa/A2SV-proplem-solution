# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_head = head
        even_head = head.next
        oddPtr = odd_head
        evenPtr = even_head
        while evenPtr and evenPtr.next:
            oddPtr.next = evenPtr.next
            oddPtr = oddPtr.next
            evenPtr.next = oddPtr.next
            evenPtr = evenPtr.next
        oddPtr.next = even_head
        return head