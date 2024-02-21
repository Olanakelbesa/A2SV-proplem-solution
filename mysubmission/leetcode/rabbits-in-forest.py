class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_r = defaultdict(int)

        total_r = 0
        for ans in answers:
            count_r[ans] += 1
        for c, count in count_r.items():
            total_r += math.ceil(count / (c + 1)) * (c + 1) 

        return total_r