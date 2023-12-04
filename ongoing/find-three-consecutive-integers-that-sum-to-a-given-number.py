class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        L =[]
        if num%3==0:
            n=num//3
            L.append(n-1)
            L.append(n)
            L.append(n+1)
            return L
        else:
            return L