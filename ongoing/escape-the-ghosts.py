class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        def time(x,y):
            a,b = target
            return max(x,a)-min(x,a) + max(y,b)-min(y,b)
        
        t_p = time(0,0)
        for a,b in ghosts:
            if time(a,b)<= t_p :
                return False 
        return True  