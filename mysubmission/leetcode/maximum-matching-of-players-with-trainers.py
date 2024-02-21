class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p = 0
        t = 0
        mat = 0
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                mat += 1
                t+=1
                p += 1
            else:
                t += 1
        return mat