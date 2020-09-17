class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        swap, keep = 1, 0
        length = len(A)
        for i in range(1, length):
            swap_prev, keep_prev = swap, keep
            swap, keep = length, length
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep = keep_prev
                swap = swap_prev + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                swap = min(swap, keep_prev + 1)
                keep = min(keep, swap_prev)
        return min(swap, keep)
