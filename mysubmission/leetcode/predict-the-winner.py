class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(left, right, turn):
            if left == right:
                if turn:
                    return [nums[left], 0]
                else:
                    return [0, nums[right]]
            if turn:
                left_store = solve(left+1, right, not turn)
                right_store = solve(left, right-1, not turn)
                left_store[0] += nums[left]
                right_store[0] += nums[right]
                if left_store[0] > right_store[0]:
                    return left_store
                else: 
                    return right_store 
            else:
                left_store = solve(left+1, right, not turn)
                right_store = solve(left, right-1, not turn)
                left_store[1] += nums[left]
                right_store[1] += nums[right]
                if left_store[1] > right_store[1]:
                    return left_store
                else: 
                    return right_store 

        ans = solve(0, len(nums)-1, True)
        return ans[0] >= ans[1]


        # def calc(l, r):
        #     if l == r:
        #         return nums[l]
        #     left = nums[l] - calc(l+1, r)
        #     right = nums[r] - calc(l, r-1)
        #     return max(left, right)
        # return calc(0, len(nums)-1) >= 0