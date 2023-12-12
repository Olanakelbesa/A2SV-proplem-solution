class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split(" ")
        remove_space = []
        reverse = []
        n = len(result)
        for i in range(n):
            if result[i] != "":
                remove_space.append(result[i])
        l_r = len(remove_space)
        for i in range(l_r):
            reverse.append(remove_space[l_r-i-1])
        output = " ".join(reverse)
        return output
