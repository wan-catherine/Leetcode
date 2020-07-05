import collections


class Solution(object):
    def largestOverlap_brute_force(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        length = len(A)
        res = 0
        for dx in range(-length+1, length):
            for dy in range(-length+1, length):
                count = 0
                for ax in range(length):
                    bx = ax + dx
                    if bx < 0 or bx >= length:
                        continue
                    for ay in range(length):
                        by = ay + dy
                        if by < 0 or by >= length:
                            continue
                        if A[ax][ay] + B[bx][by] == 2:
                            count += 1
                res = max(res, count)
        return res

    """
    Transform 2-dimension matrix int 1-dimension array!!!
    
    i - j means move j - i steps for array!
    
    Genius
    """
    def largestOverlap(self, A, B):
        length = len(A)
        la = [i // length * 100 + i % length for i in range(length * length) if A[i // length][i % length]]
        lb = [i // length * 100 + i % length for i in range(length * length) if B[i // length][i % length]]
        c = collections.Counter(i - j for i in la for j in lb)
        return max(c.values() or [0])