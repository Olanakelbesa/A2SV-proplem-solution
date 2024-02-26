class Solution:
    def countGoodNumbers(self, n: int) -> int:
            if n % 2 == 0:
                even = n // 2
            else:
                even = math.ceil(n / 2)
            odd = n // 2
            def powerFun(base, n):
                if n == 1:
                    return base
                if n == 0:
                    return 1
                if n % 2 == 0:
                    num = powerFun(base, n // 2)
                    return (num**2) % ((10**9)+7)
                else:
                    num = powerFun(base, n // 2)
                    return ((num**2)*base) % ((10**9)+7)
            return ((powerFun(5, even)) if (powerFun(5, even)) else 1) * powerFun(4, odd) % ((10**9)+7)