class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        sum_left = defaultdict(int)
        cnt_left = defaultdict(int)

        for i, num in enumerate(nums):
            ans[i] += cnt_left[num] * i
            ans[i] -= sum_left[num]

            cnt_left[num] += 1
            sum_left[num] += i

        sum_right = defaultdict(int)
        cnt_right = defaultdict(int)

        for i, num in reversed(list(enumerate(nums))):
            ans[i] += sum_right[num]
            ans[i] -= cnt_right[num] * i

            cnt_right[num] += 1
            sum_right[num] += i
        return ans

         