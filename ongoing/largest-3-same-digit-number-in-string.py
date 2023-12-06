class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i] == num[i+2]:
                result = max(result, int(num[i]))
        if result == -1:
            return ""
        else:
            return str(result) * 3
