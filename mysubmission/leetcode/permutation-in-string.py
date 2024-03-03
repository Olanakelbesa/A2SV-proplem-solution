class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        dic_s1 = Counter(s1)

        for i in range(len(s2)):
            dic_s2 = Counter(s2[i:i+k])
            if dic_s2 == dic_s1:
                return True
        return False