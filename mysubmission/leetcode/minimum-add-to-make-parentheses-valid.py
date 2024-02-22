class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openPer = 0
        closePer = 0
        for c in s:
            if c == '(':
                openPer += 1
            elif c == ')' and openPer > 0:
                openPer -= 1

            else:
                closePer += 1
        return openPer + closePer
            

#  ()))((
#  ^
#o=3 
#c=3