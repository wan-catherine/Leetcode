class Solution(object):
    def longestMountain_onepass_bymyself(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        length = len(A)
        if length < 3:
            return 0

        res, temp = 1, 1
        value= A[0]
        for i in range(1, length):
            A[i], value = A[i] - value, A[i]

            if A[i] > 0:
                if A[i-1] < 0:
                    temp = 2
                else:
                    temp += 1
            elif A[i] < 0:
                if temp > 1:
                    temp += 1
                res = max(res, temp)
            else:
                temp = 1
        return res if res > 2 else 0

    """
    In this problem, we take one forward pass to count up hill length (to every point).
    We take another backward pass to count down hill length (from every point).
    Finally a pass to find max(up[i] + down[i] + 1) where up[i] and down[i] should be positives.
    """
    def longestMountain_twopass(self, A):
        up, down = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: up[i] = up[i - 1] + 1
        for i in range(len(A) - 1)[::-1]:
            if A[i] > A[i + 1]: down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])




