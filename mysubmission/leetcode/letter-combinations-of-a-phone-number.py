class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        res = []

        def backTrack(idx, substr):
            if len(substr) == len(digits):
                if not substr:
                    return
                res.append(''.join(substr[:]))
                return
            if idx > len(digits):
                return
            for i in range(idx, len(digits)):
                string = dic[digits[i]]
                for j in range(len(string)):
                    substr.append(string[j])
                    backTrack(i + 1, substr)
                    substr.pop()
        backTrack(0, [])
        return res