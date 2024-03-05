class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backTrack(idx, path):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(idx, len(candidates)):
                if sum(path) > target: continue
                if i > idx and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                backTrack(i + 1, path)
                path.pop()

        backTrack(0, [])
        return res