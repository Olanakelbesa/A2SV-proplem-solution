class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        arr=[]
        half =int(num//3)-3
        last = int(num//3) + 3
        for i in range(half, last):
           if i +(i+1) + (i+2) == num:
                arr.append(i)
                arr.append(i+1)
                arr.append(i+2)
                return arr
        return arr