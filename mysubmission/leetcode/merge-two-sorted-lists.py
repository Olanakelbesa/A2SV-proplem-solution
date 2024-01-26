# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2
        ptr = ListNode()
        temp = ptr
        while first and second:
            if first.val <= second.val:
                ptr.next = first
                first = first.next
                ptr = ptr.next
            else:
                ptr.next = second
                second = second.next
                ptr = ptr.next
        if first:
            ptr.next = first
        else:
            ptr.next = second
        return temp.next
        
