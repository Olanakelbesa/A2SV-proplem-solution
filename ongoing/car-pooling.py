class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ld=-1
        for i in trips:
            ld=max(ld,i[2])
           
        ev=[0]*(ld+1)
        for pas,st,en in trips:
            ev[st]+=pas
            ev[en]-=pas
        if ev[0]>capacity:
            return False
        for i in range(1,len(ev)):
            ev[i]=ev[i]+ev[i-1]
            if ev[i]>capacity:
                return False
        return True