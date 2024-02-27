class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s, i):
            substr = ''
            k = 0
            while i < len(s):
                if s[i] == '[':
                    decoded_str, i = helper(s, i+1)
                    substr += k*decoded_str
                    k = 0
                elif s[i] == ']':
                    return substr, i
                elif s[i].isdigit():
                    k = k*10+int(s[i])
                else:
                    substr += s[i]
                i += 1
            return substr, i
        return helper(s, 0)[0]

