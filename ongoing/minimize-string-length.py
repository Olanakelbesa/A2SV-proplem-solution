class Solution:
    def minimizedStringLength(self, s: str) -> int:
        my_set = set()
        n = len(s)
        for i in range(n):
            my_set.update(s[i])
        print(my_set)
        return len(my_set)
            
