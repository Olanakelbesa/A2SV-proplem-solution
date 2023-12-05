class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        sumSalary=sum(salary)
        maxSalary=max(salary)
        minSalary=min(salary)
        sizeSalary=float(len(salary)-2)
               
        return (sumSalary-maxSalary-minSalary) / sizeSalary