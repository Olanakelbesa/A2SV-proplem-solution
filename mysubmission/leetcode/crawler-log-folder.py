class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if logs[i] != '../' and logs[i] != './':
                stack.append(logs[i])
            elif stack and logs[i] == '../':
                stack.pop()
            else:
                continue
        return len(stack)