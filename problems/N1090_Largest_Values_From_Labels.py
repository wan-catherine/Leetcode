import collections


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        length = len(values)
        value_label = []
        for i in range(length):
            value_label.append((values[i], labels[i]))
        value_label.sort(key=lambda x:x[0], reverse=True)

        used = collections.defaultdict(int)
        res = 0
        for value, label in value_label:
            if num_wanted == 0:
                break

            if used[label] < use_limit:
                res += value
                num_wanted -= 1
                used[label] += 1
            else:
                continue
        return res


