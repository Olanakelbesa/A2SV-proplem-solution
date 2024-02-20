class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)
        amount = tasks[0][1]
        min_e = tasks[0][1]
        for i in range(len(tasks)):
            if tasks[i][1] >= min_e:
                amount += tasks[i][1] - min_e
                min_e = tasks[i][1] - tasks[i][0]
            else:
                min_e -= tasks[i][0]

        return amount