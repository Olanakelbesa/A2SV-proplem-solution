class Solution:
    def minChanges(self, s: str) -> int:
        cnt = 0
        i = 0
        s = list(s)
        while i < len(s):
            if i + 1 <= len(s) and s[i] != s[i+1]:
                s[i+1] = s[i]
                cnt += 1
            i += 2
        return cnt