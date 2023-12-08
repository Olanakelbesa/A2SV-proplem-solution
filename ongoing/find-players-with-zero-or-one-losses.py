class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        dic=defaultdict(lambda:[0,0])
        for a in matches:
            dic[a[0]][0]+=1
            dic[a[1]][1]+=1
        ans=[[],[]]
        for a in dic:
            if(dic[a][1]==0):
                ans[0].append(a)
            if(dic[a][1]==1):
                ans[1].append(a)
        ans[0].sort()
        ans[1].sort()
        return ans