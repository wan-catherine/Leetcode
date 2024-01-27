from collections import deque
from typing import List


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

    '''
    original arr:
    [1, 0, 2, 0, 3, 0]
    num of zeros so far:
    [0, 1, 1, 2, 2, 3]
    arr with duplicate 0s (Θ means a duplicate 0):
    [1, Θ, 0, 2, Θ, 0, 3, Θ, 0]
    arr after cutoff
    [1, Θ, 0, 2, Θ, 0]
    
    # Every number in the original array is shifted to the right by the number of zeros so far.
    # Because of the cutoff, we are going to check if the new position of the number is inside the array.
    if i + zeroes < n:
    
    # This is checking if there is a Θ that should be included.
    if arr[i] == 0:
      zeroes -= 1
      if i + zeroes < n:
         arr[i + zeroes] = 0
    '''
    def duplicateZeros_2024(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0