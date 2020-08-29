import collections


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        b_mapping = collections.defaultdict(int)
        for word in B:
            word_count = collections.Counter(word).most_common()
            for a, num in word_count:
                if num > b_mapping[a]:
                    b_mapping[a] = num

        res = []
        for word in A:
            w_mapping = collections.Counter(word)
            flag = True
            for a, num in b_mapping.items():
                if a not in w_mapping or w_mapping[a] < num:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res


