import collections


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        self.length = len(pattern)
        p_intervals, p_mapping = self.get_intervals(pattern)
        res = []
        for word in words:
            if len(set(word)) != len(set(pattern)):
                continue
            w_intervals, w_mapping = self.get_intervals(word)
            if w_intervals != p_intervals:
                continue
            flag = True
            for _, intervals in p_mapping.items():
                l = len(intervals)
                if l == 1:
                    continue
                first = word[intervals[0][0]]
                for i in range(1, l):
                    if word[intervals[i][0]] != first:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                res.append(word)

        return res

    def get_intervals(self, word):
        intervals = []
        mapping = collections.defaultdict(list)
        start, end = 0, 0
        while end < self.length:
            if word[start] != word[end]:
                intervals.append((start, end - 1))
                mapping[word[start]].append((start, end-1))
                start = end
            end += 1
        intervals.append((start, self.length - 1))
        mapping[word[start]].append((start, self.length - 1))
        return intervals, mapping


