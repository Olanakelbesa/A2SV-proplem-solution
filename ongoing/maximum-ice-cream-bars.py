class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = int(1e5)+1
        counting = [0] * n

        for c in costs:
            counting[c] += 1

        cnt = 0
        for i in range(1, n):
            if counting[i] == 0:
                continue

            if coins >= i:
                usable = min(coins // i, counting[i])
                cnt += usable
                coins -= usable * i
            else:
                break

        return cnt