from collections import deque


class Solution(object):
    def duplicateZeros_my_solution(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return arr
        i = 0
        arr_len = len(arr)
        while i < arr_len:
            if arr[i] != 0:
                i += 1
                continue
            for j in range(arr_len-2, i, -1):
                arr[j+1] = arr[j]
            if i + 1 < arr_len:
                arr[i+1] = 0
            i += 2

    def duplicateZeros(self, arr):
        isZero = False
        q = deque()

        for i in range(len(arr)):
            if isZero:
                q.append(arr[i])
                arr[i] = 0
                isZero = False
            else:
                q.append(arr[i])
                arr[i] = q.popleft()
                if arr[i] == 0:
                    isZero = True