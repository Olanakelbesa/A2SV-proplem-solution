class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix = [0]*(n+1)
        cur = 0
        for i in range( n):
            cur += nums[i]
            self.prefix[i+1]=cur
        print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)