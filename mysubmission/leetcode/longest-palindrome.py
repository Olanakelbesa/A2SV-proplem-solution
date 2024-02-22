class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_char = Counter(s)
        odd = []
        even = []
        for c in count_char:
            if count_char[c] % 2 == 0:
                even.append(count_char[c])
            else:
                odd.append(count_char[c])
        if odd:
           odd_sum = sum(odd) - (len(odd) - 1)
           return odd_sum + sum(even) 
        else:
            return sum(even)
