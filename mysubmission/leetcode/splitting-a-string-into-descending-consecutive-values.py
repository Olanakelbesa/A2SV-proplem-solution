class Solution:
    def splitString(self, s: str) -> bool:
        cur = []
        def backtrack(idx):
            if idx >= len(s):
                return len(cur) >= 2
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if len(cur) == 0 or val == cur[-1] - 1:
                    cur.append(val)
                    if backtrack(i +1):
                        return True
                    cur.pop()
            return False
        return backtrack(0)