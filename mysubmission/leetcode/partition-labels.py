class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l, r = 0, 0
        res = []
        dic = {}
        max_ = 0
        for i in range(len(s)):
            dic[s[i]] = i
        for r in range(len(s)):
            max_ = max(max_, dic[s[r]])
            if r == max_:
                res.append(r - l + 1)
                l = r + 1
        return res