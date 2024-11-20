class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limit = Counter(s)
        for ch in "abc":
            if limit[ch] < k: return -1
            limit[ch] -= k

        maxWindow, l = 0, 0
        curWindow = defaultdict(int)

        for r in range(len(s)):
            curWindow[s[r]] += 1
            while curWindow[s[r]] > limit[s[r]]:
                curWindow[s[l]] -= 1
                l += 1
            maxWindow = max(maxWindow, r - l + 1)
        return len(s) - maxWindow