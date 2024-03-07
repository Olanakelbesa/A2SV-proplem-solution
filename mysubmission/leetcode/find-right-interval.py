class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def helper(sorted_int, end):
            left, right = 0, len(sorted_int) - 1
            res = -1
            
    
            while left <= right:
                mid = (left + right) // 2
                if sorted_int[mid][0] >= end:
                    res = sorted_int[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            return res

        sorted_int = []
        for i, interval in enumerate(intervals):
            sorted_int.append((interval[0], i))
        sorted_int.sort(key = lambda x:x[0])
        
        ans = []
        for interval in intervals:
            res = helper(sorted_int, interval[1])
            ans.append(res)
        return ans
