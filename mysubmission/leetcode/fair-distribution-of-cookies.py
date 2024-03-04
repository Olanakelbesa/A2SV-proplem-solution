class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        self.minUnfairness = float('inf')
        cookies.sort(reverse = True)
        def backTrack(idx):
            if idx >= len(cookies):
                self.minUnfairness = min(self.minUnfairness, max(bucket))
                return 
            if max(bucket) > self.minUnfairness:
                return
            for j in range(k):
                bucket[j] += cookies[idx]
                backTrack(idx + 1)
                bucket[j] -= cookies[idx]
        backTrack(0)
        return self.minUnfairness