class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        set_card = set(fronts + backs)
        print(set_card)
        for f, b in zip(fronts, backs):
            if f == b:
                set_card.discard(f)
        print(set_card)
        return min(set_card, default = 0)