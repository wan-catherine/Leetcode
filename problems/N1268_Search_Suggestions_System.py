import bisect
import collections


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        length = len(searchWord)
        res = [[] for _ in range(length)]
        for word in products:
            index = self.check(word, searchWord)
            if index == 0:
                continue
            for i in range(index):
                bisect.insort_left(res[i], word)
        for i in range(length):
            res[i] = res[i][:3]
        return res

    def check(self, word, searchWord):
        w_len, s_len = len(word), len(searchWord)
        for i in range(w_len):
            if i >= s_len or word[i] != searchWord[i]:
                break
        if i < w_len - 1:
            return i
        if i == w_len - 1:
            if i >= s_len:
                return s_len
            if word[i] != searchWord[i]:
                return i
            return w_len