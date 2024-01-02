class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum=0
        piles.sort()
        print(piles)
        for i in range(len(piles)//3):
            sum+=piles[-i*2-2]
            print(sum)
        return sum