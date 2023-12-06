class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        div = n // 7
        rem = n % 7
        result = 0
        week = []
        if n > 7:
            for i in range(div):
                week.append(28 + 7*i)
        remain = div
        week2 = []
        for i in range(rem):
            week2.append(div + i + 1)
        result = sum(week) + sum(week2)
        return result

        


