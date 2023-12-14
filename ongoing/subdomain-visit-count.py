class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_domain = {}
        for dom in cpdomains:
            num, domain = dom.split(" ")
            num = int(num)
            domain = list(domain.split("."))
            for i in range(len(domain)):
                temp = ".".join(domain[i:])
                count_domain[temp]=count_domain.get(temp,0)+num
            ans=[]
            for i,j in count_domain.items():
                te=str(j)+" "+i
                ans.append(te)
        return ans


        