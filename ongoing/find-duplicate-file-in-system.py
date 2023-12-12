class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for path in paths:
            l = path.split()
            for i in range(1, len(l)):
                name, cont = l[i].split("(")
                result[cont[:-1]].append(l[0] + "/" + name)
                
        return [i for i in result.values() if len(i) > 1]