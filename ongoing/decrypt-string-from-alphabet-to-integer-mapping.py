class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s
