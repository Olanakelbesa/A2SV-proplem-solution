# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        elif head.next == None:
            return head
        else:
            first = head
            second = head.next
            while second:
                if first.val == second.val:
                    first.next = second.next
                    second = first.next
                else:
                    first = first.next
                    second = second.next
            return head
