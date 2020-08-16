class Solution(object):
    def longestOnes_compare(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        res, k = 0, K
        start, end = 0, 0
        while end < length:
            if A[end] == 0:
                k -= 1
            if k < 0:
                while A[start] == 1:
                    start += 1
                start += 1
                k += 1
            end += 1
            res = max(res, end - start)
            print(f"{start},{end},{res}")
        return res

    """
    No need a inner loop for find the next A[start] == 1
    If we find a bigger window, we use this window to iterate till we find a larger one if there has . 
    """
    def longestOnes(self, A, K):
        length = len(A)
        start, end = 0, 0
        while end < length:
            if A[end] == 0:
                K -= 1
            # when k < 0  start and end all + 1, so the window's length keep the same.
            if K < 0:
                if A[start] == 0:
                    K += 1
                start += 1
            end += 1
        return end - start

