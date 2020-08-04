import collections


class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words_set = set(words)
        words_sort = sorted(words_set, key=lambda word: len(word))

        memo = collections.defaultdict(int)
        res = 1
        for word in words_sort:
            word_len = len(word)
            if word_len == 1:
                memo[word] = 1
                continue
            for i in range(word_len):
                new_word = word[:i] + word[i+1:]
                if new_word not in words_set:
                    continue
                memo[word] = max(memo[word], memo[new_word] + 1)
            memo[word] = max(memo[word], 1)
            res = max(memo[word], res)

        return res



