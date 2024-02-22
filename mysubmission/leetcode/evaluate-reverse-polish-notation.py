class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
          if token.isnumeric() or (token[0] == '-' and token[1:].isdigit()):
              stack.append(int(token))
          elif len(stack) > 1:
              num1 = stack.pop()
              num2 = stack.pop()
              if token == '+':
                  stack.append(num2 + num1)
              elif token == '-':
                  stack.append(num2-num1)
              elif token == '*':
                  stack.append(num2 * num1)
              else:
                stack.append(int(num2/num1))
        return (stack[0])




