"""
Check all possible to get a palindrome.
The new added can be in the left or right.
We need to check all the part . Here, in order to avoid duplication, when check another side, need to add i != 0.
"""
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mapping = {}
        res = []
        for index, word in enumerate(words):
            mapping[word] = index

        for index, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):
                left, right = word[:i], word[i:]
                if left[::-1] in mapping and mapping[left[::-1]] != index and right == right[::-1]:
                    res.append([index, mapping[left[::-1]]])
                if i != 0 and right[::-1] in mapping and mapping[right[::-1]] != index and left == left[::-1]:
                    res.append([mapping[right[::-1]], index])
        return res
