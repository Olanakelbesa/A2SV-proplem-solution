class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.ptr = 0
        self.operation = [""]*n
    ptr = 3
    def insert(self, idKey: int, value: str) -> List[str]:
        self.operation[idKey - 1] = value
        lst = []
        while self.ptr < self.n:
            if self.operation[self.ptr] != "":
                lst.append(self.operation[self.ptr])
                self.ptr += 1
            else:
                self.operation[self.ptr] == 0 and self.ptr >= self.n
                break
        return lst



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)