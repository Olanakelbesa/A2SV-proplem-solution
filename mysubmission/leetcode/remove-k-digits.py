class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k-=1
            stack.append(digit)
        final_stack = stack[:-k] if k > 0 else stack
        return "".join(final_stack).lstrip("0") or "0"