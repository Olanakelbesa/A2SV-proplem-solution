class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)

        set_1 = set(nums1)
        set_2 = set(nums2)
        intersection = set_1 & set_2
        result = []
        for n in intersection:
            min_num = min(dic1[n], dic2[n])
            for i in range(min_num):
                result.append(n)
        return result
        
