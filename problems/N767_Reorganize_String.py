import collections


class Solution(object):
    def reorganizeString_my(self, S):
        """
        :type S: str
        :rtype: str
        """
        counters = collections.Counter(S)
        sorted_counters = counters.most_common()
        key_len = len(counters)
        maximum = sorted_counters[0][1]
        if 2*maximum > sum(counters.values()) + 1:
            return ""

        lists = [[sorted_counters[0][0]] for _ in range(maximum)]

        j = 1
        while j < key_len:
            for i in range(maximum):
                while True:
                    if j >= key_len:
                        break
                    if counters[sorted_counters[j][0]] > 0:
                        lists[i].append(sorted_counters[j][0])
                        counters[sorted_counters[j][0]] -= 1
                        break
                    else:
                        j += 1
                counters[sorted_counters[0][0]] -= 1

        res = ""
        for li in lists:
            res += ''.join(li)
        return res

    def reorganizeString(self, S):
        N = len(S)
        res = []
        counters = collections.Counter(S)
        sorted_counters = counters.most_common()
        for key, value in sorted_counters[::-1]:
            if 2*value > N + 1:
                return ""
            res.extend(key*value)


        # for c, x in sorted((S.count(x), x) for x in set(S)):
        #     if c > (N + 1) / 2: return ""
        #     res.extend(c * x)

        ans = [None] * N
        ans[::2], ans[1::2] = res[N//2:], res[:N//2]
        return "".join(ans)