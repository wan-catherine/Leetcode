"""
Each time, find the largest one and flip it to the top, then flip it to the bottom
The bottom line is there are only two number in the array , we can directly check and finish.
"""
class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        res = []
        if A == list(range(1,length+1)):
            return res

        self.recusive(A, res)
        return res

    def recusive(self, a, res):
        length = len(a)
        if length == 2:
            if a[0] > a[1]:
                res.append(2)
            return
        index = a.index(len(a))
        res.append(index + 1)
        a = a[:index+1][::-1]+a[index+1:]
        res.append(len(a))
        a = a[::-1][:-1]
        self.recusive(a, res)
