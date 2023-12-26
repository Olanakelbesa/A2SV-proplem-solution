class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n):
            max_index = i
            for j in range(i, n):
                if heights[j] > heights[max_index]:
                    max_index = j
            if max_index != i:
                heights[max_index], heights[i] = heights[i], heights[max_index]
                names[max_index], names[i] = names[i], names[max_index]
        print(heights)
        return names
