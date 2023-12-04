class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return("")
        if len(strs)==1:
            return(strs[0])
        
        pref = strs[0]
        plen = len(strs[0])
        
        for s in strs[1:]:
            while pref != s[:plen]:
                pref = pref[:-1]
                plen = len(pref)
                if plen ==0:
                    return("")
                
        return pref
        