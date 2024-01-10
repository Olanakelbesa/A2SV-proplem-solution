class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = (Counter(p))
        ans=[]
        for i in range( len(s)):
            target[s[i]]-=1
            if i>=len(p):target[s[i-len(p)]]+=1
            if all(target[j]==0 for j in target):ans.append(i-len(p)+1)
        # print(arr)
        return ans

