class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        index = 0
        left_max = cur_max = A[0]
        for i, num in enumerate(A):
            cur_max = max(cur_max, num)
            if num < left_max:
                left_max = cur_max
                index = i
            print(cur_max, left_max)
        return index + 1