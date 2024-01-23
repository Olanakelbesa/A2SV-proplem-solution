class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        if temp is None:
            return -1
        while temp and index:
            temp = temp.next
            index -= 1
        if temp is None:
            return -1
        return temp.data

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
            return
        newNode = Node(val)
        if self.head is None and index != 0:
            return
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        temp = self.head
        while temp and index > 1:
            temp = temp.next
            index -= 1
        if temp is None:
            return
        newNode.next = temp.next
        temp.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        while temp and index > 1:
            temp = temp.next
            index -= 1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)