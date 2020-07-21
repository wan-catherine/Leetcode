import bisect
import collections


class Solution(object):
    def invalidTransactions_slow(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        array = []
        res = []
        for tran in transactions:
            t_arr = tran.split(',')
            array.append(t_arr)

        length = len(array)
        ids = set()
        for i in range(length):
            if int(array[i][2]) > 1000:
                ids.add(i)
            for j in range(i+1, length):
                if array[i][0] == array[j][0] and array[i][3] != array[j][3] and abs(int(array[i][1]) - int(array[j][1])) <= 60:
                    ids.add(i)
                    ids.add(j)

        for i in ids:
            res.append(','.join(array[i]))
        return res

    def invalidTransactions(self, transactions):
        D = collections.defaultdict(list)
        for x in transactions:
            n, t, _, c = x.split(",")
            t = int(t)
            D[n].append((t, c))
        for n in D.keys():
            TC = sorted(D[n], key=lambda x: x[0])
            T = [t for t, c in TC]
            C = [c for t, c in TC]
            D[n] = [T, C]
        res = []
        for x in transactions:
            n, t, a, c = x.split(",")
            t = int(t)
            a = int(a)
            if a > 1000:
                res.append(x)
            else:
                T, C = D[n]
                # use bisect_left, bisect_right and break here to make sure no duplicated transaction be added into res
                lo = bisect.bisect_left(T, t - 60)
                hi = bisect.bisect_right(T, t + 60)
                for i in range(lo, hi):
                    if C[i] != c:
                        res.append(x)
                        break
        return res
