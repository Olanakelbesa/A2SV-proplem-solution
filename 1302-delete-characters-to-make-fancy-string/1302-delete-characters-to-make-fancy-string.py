class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        i = 0
        while i < len(s):
            if len(s[i:i+3]) == 3 and len(set(s[i:i+3])) == 1:
                i+=1
                continue
            else:
                ans += s[i]
                i+=1
        return ans