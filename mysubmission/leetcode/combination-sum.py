class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backTrack(path):
            if sum(path) == target:
                path = path[:]
                path.sort()
                if path not in res:
                    res.append(path)
                return

            for i in range(n):
                if sum(path) > target:
                    continue
                path.append(candidates[i])
                backTrack(path)
                path.pop()
        n = len(candidates)
        backTrack([])
        return res