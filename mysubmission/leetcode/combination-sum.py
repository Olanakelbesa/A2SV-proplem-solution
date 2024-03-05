class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backTrack(idx, path):
            if sum(path) == target:
                res.append(path[:])
                return

            for i in range(idx, len(candidates)):
                if sum(path) > target:
                    continue
                path.append(candidates[i])
                backTrack(i, path)
                path.pop()
        backTrack(0, [])
        return res