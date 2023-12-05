class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alien_dict = {char: index for index, char in enumerate(order)}

        def compare(word1, word2):
            for char1, char2 in zip(word1, word2):
                if alien_dict[char1] < alien_dict[char2]:
                    return -1
                elif alien_dict[char1] > alien_dict[char2]:
                    return 1
            return len(word1) - len(word2)

        for i in range(len(words) - 1):
            if compare(words[i], words[i + 1]) > 0:
                return False

        return True

