class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        tcount = 0
        fcount = 0

        n = len(answerKey)

        left = 0
        window_sz = 0

        for right in range(n):
            if answerKey[right] == 'T':
                tcount += 1
            else:
                fcount += 1

            while tcount > k and fcount > k:

                if answerKey[left] == 'T':
                    tcount -= 1
                else:
                    fcount -= 1
                left += 1
            
            window_sz = max(window_sz, right-left+1)

        return window_sz