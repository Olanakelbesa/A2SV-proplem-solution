class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        arr3 = []
        for i in range(len(arr2)):
            if arr2[i] in arr1:
                for _ in range(arr1.count(arr2[i])):
                    arr.append(arr2[i])
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                arr3.append(arr1[i])
        arr3.sort()
        return (arr + arr3)