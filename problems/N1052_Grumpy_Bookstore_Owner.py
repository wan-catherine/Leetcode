from typing import List


class Solution(object):
    def maxSatisfied_first_slow(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        length = len(grumpy)
        if X >= length:
            return sum(customers)

        before = 0
        res = 0
        for i in range(length):
            if grumpy[i] == 0:
                before += customers[i]
            if grumpy[i] == 0 and i + X < length:
                continue
            if i + X > length:
                break
            res = max(res, sum([customers[i] for i in range(i, i + X) if grumpy[i] == 1]))
        return before + res

    def maxSatisfied(self, customers, grumpy, X):
        length = len(grumpy)
        if X >= length:
            return sum(customers)

        before = 0
        temp = 0
        res = 0
        start, end = 0, 0
        for i in range(length):
            if grumpy[i] == 0:
                before += customers[i]
            if grumpy[i] == 1:
                temp += customers[i]
            if end >= X:
                if grumpy[start] == 1:
                    temp -= customers[start]
                start += 1
            end += 1
            res = max(res, temp)
        return res + before

    def maxSatisfied_20250217(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        length = len(customers)
        prefix = customers[:]
        for i in range(1, length):
            prefix[i] += prefix[i-1]
        prefix = [0] + prefix
        ppre = [0]
        for i in range(length):
            if grumpy[i] == 0:
                ppre.append(ppre[-1] + customers[i])
            else:
                ppre.append(ppre[-1])

        res, j = 0, 0
        for i in range(length):
            j = min(i + minutes - 1, length - 1)
            val = ppre[-1] - (ppre[j+1] - ppre[i]) + prefix[j+1] - prefix[i]
            res = max(res, val)

        return res
