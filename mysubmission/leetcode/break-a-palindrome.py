class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        pal_list = list(palindrome)
        n = len(pal_list)
        for i in range(n//2):
            if pal_list[i] != 'a':
                pal_list[i] = 'a'
                break
        else:
            pal_list[-1] = 'b' 

        return ''.join(pal_list)
