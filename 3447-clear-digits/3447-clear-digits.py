class Solution:
    def clearDigits(self, s: str) -> str:
        stuck = []
        for ch in s:
            if ch.isdigit() and stuck:
                stuck.pop()
            else:
                stuck.append(ch)
        return "".join(stuck)


        