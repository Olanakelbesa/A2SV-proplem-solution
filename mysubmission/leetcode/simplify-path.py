class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path:
            if c == '/':
                if cur == '..':
                    if stack:
                        stack.pop()
                elif cur and cur != '.': 
                    stack.append(cur)
                cur = ''
            else:
                cur += c 
        if cur:
            if cur == '..':
                if stack:
                    stack.pop()
            elif cur != '.':
                stack.append(cur)
        final_stack = '/' + '/'.join(stack)
        return final_stack