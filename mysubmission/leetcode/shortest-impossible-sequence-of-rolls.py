class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        dic = defaultdict(int)
        count = 0
        for i, roll in enumerate(rolls):
            dic[roll] += 1
            if len(dic) == k:
                count += 1
                dic.clear()
        return count+1
        