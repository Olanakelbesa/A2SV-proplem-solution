class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        res = sum(arr[:n-k])
        m = res
        for i in range(n-k, n):
            res += (arr[i] - arr[i-(n-k)])
            m = min(m, res)
        return sum(arr) - m