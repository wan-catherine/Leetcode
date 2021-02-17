class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        length = len(A)
        nums = [0] * length
        nums[0] = 1 if A[0] == 0 else 0
        res = 1 if nums[0] else 0
        for i in range(1, length):
            val = nums[i - K] if i >= K else 0
            if (A[i] == 0 and (nums[i-1] - val) % 2 == 0) or (A[i] == 1 and (nums[i-1] - val) % 2):
                if i + K > length:
                    return -1
                nums[i] = nums[i-1] + 1
                res += 1
            else:
                nums[i] = nums[i-1]
        return res