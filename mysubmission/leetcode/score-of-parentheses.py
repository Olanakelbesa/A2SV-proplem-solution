class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                score = stack.pop()
                if score == 0:
                    score = 1
                else:
                    score *= 2
                if stack:
                    stack[-1] += score
                else:
                    stack.append(score)
        return sum(stack)
            
