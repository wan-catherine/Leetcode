import collections

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(barcodes)
        keys = sorted(counter.items(), key=lambda item : item[1], reverse=True)
        res = [[] for _ in range(keys[0][1])]
        length = keys[0][1]
        index = 0
        for i, n in keys:
            while n > 0:
                index %= length
                res[index].append(i)
                index += 1
                n -= 1
        ans = []
        for li in res:
            ans.extend(li)
        return ans


