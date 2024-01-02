class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for i in range(len(s)):
            if s[i].lower() >= "a" and s[i].lower() <= "z":
                st += s[i].lower()
            if s[i] >= "0" and s[i] <= "9":
                st += str(s[i])
        n = len(st)
        l = 0
        r = n - 1
        while l < r:
            if st[l] != st[r]:
                return False
            l+=1
            r-=1
        return True     