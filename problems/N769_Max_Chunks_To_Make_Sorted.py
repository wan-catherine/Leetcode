"""
I think I get it now .
so the number in arr all among 0 ~ 9
and an array arr that is a permutation of [0, 1, ..., arr.length - 1]
so at sorted status, the index of the number equals to number itself.
at this situation, we can split it into arr.length.

We can get from 0 ~ i  the maximum number .
when max_li[i] == i, it means , for 0 ~ i, we can get a chunk.

in order to get the maximum chunks, so we can just add them.

"""
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        arr_len = len(arr)
        max_li = [-1] + [0]* arr_len
        for i in range(arr_len):
            max_li[i+1] = max(max_li[i], arr[i])
            if i == max_li[i+1]:
                count += 1
        return count
