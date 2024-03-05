class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backTrack(idx, path):
            if len(path) == k and sum(path) == n:
                res.append(path[:])
                return
            for i in range(idx, 10):
                # if sum(path) > n and len(path) > k:
                #     continue
                path.append(i)
                backTrack(i+1, path)
                path.pop()
        backTrack(1, [])
        return res
