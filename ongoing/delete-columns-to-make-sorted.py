class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        lst = [list(string) for string in strs]
        column = list(zip(*lst))
        
        count = 0
        for ch in column:
            conc = "".join(ch)
            if conc !="".join(sorted(conc)):
                count += 1
        return count


           