"""
Each time, find the largest one and flip it to the top, then flip it to the bottom
The bottom line is there are only two number in the array , we can directly check and finish.
"""
from typing import List


class Solution(object):
    def pancakeSort_before(self, A):
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

    def pancakeSort(self, A):
        res = []
        self.helper(A, res)
        return res

    def helper(self, arr, res):
        sort_arr = sorted(arr)
        if sort_arr == arr:
            return
        stack = []
        for i, val in enumerate(arr):
            while stack and arr[stack[-1]] < val:
                stack.pop()
            stack.append(i)
        length = len(stack)
        arr_len = len(arr)
        if length == arr_len:
            res.append(length)
            return

        if stack[0] == arr_len - 1:
            self.helper(arr[:-1], res)
        elif stack[0] == 0:
            res.append(arr_len)
            arr = arr[::-1]
            self.helper(arr[:-1], res)
        else:
            res.append(stack[0] + 1)
            arr = arr[:stack[0] + 1][::-1] + arr[stack[0] + 1:]
            arr = arr[::-1]
            res.append(arr_len)
            self.helper(arr[:-1], res)

    def pancakeSort_20220531(self, arr: List[int]) -> List[int]:
        res = []
        length = len(arr)
        sarr = sorted(arr)
        for i in range(length - 1, -1, -1):
            num = sarr[i]
            for j in range(length):
                if num == arr[j]:
                    if j < i:
                        res.append(j + 1)
                        arr = arr[:j + 1][::-1] + arr[j + 1:]
                        res.append(i + 1)
                        arr = arr[:i + 1][::-1] + arr[i + 1:]
                    break
        return res