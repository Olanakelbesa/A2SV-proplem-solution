class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        max_index = arr.index(max(arr))
        if max_index == 0 or max_index == n-1:
            return False
        for i in range(max_index):
            if arr[i] >= arr[i+1]:
                return False
        for i in range(max_index, n-1):
            if arr[i] <= arr[i+1]:
                return False
        return True
