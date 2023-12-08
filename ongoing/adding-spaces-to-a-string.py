class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result_parts = []
        st = 0
        for num in spaces:
            if st < len(s) and num <= len(s):
                result_parts.append(s[st:num])
                result_parts.append(" ")
                st = num
            else:
                break
        result_parts.append(s[st:])
        
        result_str = ''.join(result_parts)
        print(result_str)
        return result_str
