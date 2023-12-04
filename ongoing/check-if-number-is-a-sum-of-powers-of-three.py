class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1 and n % 3 != 2:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
        return n == 1