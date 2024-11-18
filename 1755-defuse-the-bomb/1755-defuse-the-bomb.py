class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypt = [0 for _ in range(n)]
        if k > 0:
           for i in range(n):
                _sum = 0
                j = i
                for _ in range(k):
                    j += 1
                    _sum += code[j % n]
                decrypt[i] = _sum
        if k < 0:
            for i in range(n):
                _sum = 0
                j = i
                for _ in range(abs(k)):
                    j -= 1
                    _sum += code[j % n]
                decrypt[i] = _sum
        return decrypt
