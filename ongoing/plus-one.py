class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        st = "".join(map(str, digits))
        last_sum = int(st) + 1
        my_digits = [int(digit) for digit in str(last_sum)]
        return my_digits

        
