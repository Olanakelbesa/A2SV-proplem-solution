class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        for booking in bookings:
            first, last, seats = booking
            ans[first-1] += seats
            ans[last] -= seats
        for i in range(1, n):
            ans[i] += ans[i-1]
        return ans[:n]

