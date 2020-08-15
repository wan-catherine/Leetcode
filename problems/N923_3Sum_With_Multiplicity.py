import collections


class Solution(object):
    def threeSumMulti_slow(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        length = len(A)
        if length < 3:
            return 0

        A.sort()
        res = 0
        for i in range(length - 1, 1, -1):
            if A[i] > target:
                continue
            start, end = 0, i - 1
            while start < end:
                value = A[start] + A[end] + A[i]
                if value == target:
                    if A[start] == A[end]:
                        res += (end - start + 1) * (end - start) // 2
                        break
                    p, q = 0, 0
                    while A[start + p] == A[start]:
                        p += 1
                    while A[end - q] == A[end]:
                        q += 1

                    res += p * q
                    start = start + p
                    end = end - q
                elif value < target:
                    start += 1
                else:
                    end -= 1
        return res % (10 ** 9 + 7)

    """
    Loop i on all numbers,
    loop j on all numbers,
    check if k = target - i - j is valid.

    Add the number of this combination to result.
    3 cases covers all possible combination:
        1. i == j == k
        2. i == j != k
        3. i < k && j < k 
    
    Key point is to keep : i <= k and j <= k . 
    """
    def threeSumMulti(self, A, target):
        counts = collections.Counter(A)
        res = 0
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k > 100 or k < 0:
                    continue
                if i == j and j == k:
                    res += counts[i] * (counts[i] - 1) * (counts[i] - 2) // 6
                elif i == j:
                    res += counts[i] * (counts[i] - 1) * counts[k] // 2
                elif i < k and j < k:
                    res += counts[i] * counts[j] * counts[k]
        return res % (10 ** 9 + 7)

