class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        dic = {}
        i, j, res = 0, 0, 0
        while j < n:
            dic.setdefault(fruits[j], 0)
            dic[fruits[j]] += 1
            if len(dic) < 3: 
                res = max(res, j - i + 1)
            else:
                dic[fruits[i]] -= 1
                if dic[fruits[i]] == 0:
                    dic.pop(fruits[i])
                i += 1
            j += 1
        return res