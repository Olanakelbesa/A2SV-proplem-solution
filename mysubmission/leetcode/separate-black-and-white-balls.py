class Solution:
    def minimumSteps(self, s: str) -> int:
        blacks = 0
        res = 0
        for c in s:
            if c=='1':
                blacks += 1
            else:
                res += blacks
        return res