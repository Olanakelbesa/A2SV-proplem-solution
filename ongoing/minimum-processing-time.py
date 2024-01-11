class Solution:
	def minProcessingTime(self, proTime: List[int], tasks: List[int]) -> int:

		res = 0
		proTime = sorted(proTime)
		tasks = sorted(tasks , reverse = True)
		i = 0
		for pro in proTime:
			count = 0
			current_max = 0
			while i < len(tasks):
				if count == 4:
					break
				current_max = max(current_max , pro + tasks[i])
				count = count + 1
				i = i + 1
			res = max(res , current_max)
		return res