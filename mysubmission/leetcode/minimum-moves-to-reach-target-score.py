class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target != 1 and maxDoubles != 0:
            if target % 2 != 0:
                ans += 1
                target -= 1
            target /= 2
            ans += 1
            maxDoubles -= 1
        if target != 1:
            ans += math.ceil(target - 1)
        return ans