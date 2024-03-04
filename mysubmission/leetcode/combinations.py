class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first, path):
            if len(path) == k:
                ans.append(path[:])
            for num in range(first, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
        ans = []
        backtrack(1, [])
        return ans