import collections
"""
Bucket sort
Similar as problem 347
"""

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_count_mapping = collections.defaultdict(int)
        for word in words:
            word_count_mapping[word] += 1

        max_frequent = 0
        frequent_word_mapping = collections.defaultdict(list)
        for key, value in word_count_mapping.items():
            max_frequent = max(max_frequent, value)
            frequent_word_mapping[value].append(key)

        res = []
        while max_frequent > 0:
            if not frequent_word_mapping[max_frequent]:
                max_frequent -= 1
                continue
            length = len(frequent_word_mapping[max_frequent])
            if k >= length:
                k -= length
                res.extend(sorted(frequent_word_mapping[max_frequent]))
                max_frequent -= 1
            else:
                frequent_word_mapping[max_frequent].sort()
                res.extend(frequent_word_mapping[max_frequent][:k])
                break
        return res