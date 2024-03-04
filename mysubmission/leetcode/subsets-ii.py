class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        nums.sort()
        def backTrack(idx, path, length):
            if len(path) == length and path[:] not in res:
                res.append(path[:])
                return

            for i in range(idx, n):
                path.append(nums[i])
                backTrack(i + 1, path, length)
                path.pop()
        for i in range(1, n+1):
            backTrack(0, [], i)
        return res