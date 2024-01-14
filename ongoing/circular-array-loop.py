class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        def helper(index):
            return (nums[index]+index)%len(nums)
        visited = set()

        for i in range(len(nums)):
            if i in visited:
                continue
            slow, fast= i, helper(i)
            while True:
                if nums[slow]*nums[fast]>0 and nums[helper(fast)]*nums[fast]>0:
                    slow, fast = helper(slow), helper(helper(fast))
                    visited.add(slow)
                    if fast==slow:
                        if fast!=helper(fast):
                            return True
                        break
                else:
                    break
        return False