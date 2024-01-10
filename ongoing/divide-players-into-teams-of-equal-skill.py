class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        i = 0
        j = n - 1
        target = skill[0] + skill[n-1]
        chem = 0
        while i < j:
            if (skill[i] + skill[j]) != target:
                return -1
            chem += skill[i] * skill[j]
            i += 1
            j -= 1
        return chem