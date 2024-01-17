class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n, m= len(s), len(shifts)
        prefix_sum = [0]*n
        nums = [0]*(n+1)
        sum_ = 0
        arr = ""
        for i in range(m):
            left = shifts[i][0]
            right =  shifts[i][1]
            k = 1 if shifts[i][2] == 1 else -1
            nums[left] += k
            nums[right+1] -= k
        for i in range(n):
            sum_ += nums[i]
            prefix_sum[i] = sum_ 
        for i in range(n):
            ab = ((ord(s[i]) + prefix_sum[i] - 97)%26) + 97
            arr += chr(ab)
        return arr
