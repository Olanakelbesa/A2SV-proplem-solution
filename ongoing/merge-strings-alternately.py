class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        count = 0
        merge = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                merge += word1[i] +word2[i]
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                merge += word1[i] +word2[i]
                count += 1
            for i in range(count, len(word2)):
                merge += word2[i]
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                merge += word1[i] +word2[i]
                count += 1
            for i in range(count, len(word1)):
                merge += word1[i]
        
        return merge
        
        

        