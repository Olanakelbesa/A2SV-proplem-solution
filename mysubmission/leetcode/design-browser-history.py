class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        self.current.next = ListNode(url, self.current)
        self.current = self.current.next

    def back(self, steps: int) -> str:
        count = 0
        while count < steps and self.current.prev:
            self.current = self.current.prev
            count += 1
        return self.current.val

    def forward(self, steps: int) -> str:
        count = 0
        while count < steps and self.current.next:
            self.current = self.current.next
            count += 1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)