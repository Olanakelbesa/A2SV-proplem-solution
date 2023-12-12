class Solution:
	def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
		start=0
		for i in nums:
			if i % 2==0:
				start+=i

		result=[]
		for i in queries:
			num,index=i
			nums[index]+=num
			if nums[index]%2==0 and num%2==0:
				start+=num
			if nums[index]%2==0 and num%2==1:
				start+=nums[index]
			if nums[index]%2==1 and num%2==1:
				start-=(nums[index]-num)
			result.append(start)
		return result