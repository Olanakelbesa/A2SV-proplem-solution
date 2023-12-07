class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        lst = []

        for i in range(len(boxes)):
            add_ball = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    add_ball += (abs(i - j))
            lst.append(add_ball)
        return lst
                    