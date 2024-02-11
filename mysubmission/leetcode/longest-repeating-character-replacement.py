class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        frequency = {}
        longest_str_len = 0
        for r in range(len(s)):
            
            if not s[r] in frequency:
                frequency[s[r]] = 0
            frequency[s[r]] += 1
            
            cells_count = r - l + 1
            if cells_count - max(frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)
                
            else:
                frequency[s[l]] -= 1
                if not frequency[s[l]]:
                    frequency.pop(s[l])
                l += 1
        
        return longest_str_len
		
        