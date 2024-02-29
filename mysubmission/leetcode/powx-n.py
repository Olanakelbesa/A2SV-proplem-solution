class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if  x== 0: return 0
            if n == 0: return 1

            if n % 2:
                res = power(x, n // 2)
                return (res**2) * x
            else:
                res = power(x, n // 2)
                return res*res
        ans = power(x, abs(n))
        return ans if n >= 0 else (1 / ans)
        
        