class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = {}
        n = len(arr)
        for num in arr: 
            dic.update({num: arr.count(num)})
            if dic[num] / n > 0.25:
                return num
