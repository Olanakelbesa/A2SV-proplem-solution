class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = s.count('0')
        one = len(s) - zero
        zeroPrefix = onePrefix = res = 0
        for i in s:
            if i == '0':
                res += onePrefix * (one - onePrefix)
                zeroPrefix += 1
            else:
               res += zeroPrefix * (zero - zeroPrefix)
               onePrefix += 1 
        return res