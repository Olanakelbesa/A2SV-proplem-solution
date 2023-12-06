class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_sum = {} 
        result = []

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index_sum[list1[i]] = i + j

        min_index_sum = min(index_sum.values())

        for restaurant, sum_num in index_sum.items():
            if sum_num == min_index_sum:
                result.append(restaurant)

        return result
