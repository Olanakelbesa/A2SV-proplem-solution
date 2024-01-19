class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        pre = 0
        res = 0
        for i in nums:
            pre += i
            if (pre % k) in dic:
                res += dic[pre % k]
            dic[pre % k] += 1
        return res