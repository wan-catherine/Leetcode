import collections
from typing import List


class Solution:
    def threeEqualParts_before(self, arr: List[int]) -> List[int]:
        zero = 0
        for i in arr:
            if i == 1:
                break
            zero += 1
        flag = True
        if zero > 3:
            flag = False
            arr = arr[zero - 3:]
        length = len(arr)
        l = collections.defaultdict(list)
        cur, total = 0, 0
        for i in range(length - 2):
            cur = cur * 2 + arr[i]
            l[cur].append(i)
        total = cur
        for i in arr[length - 2:]:
            total = total * 2 + i

        cur = 0
        for i in range(length - 1, 1, -1):
            cur += arr[i] * (1 << (length - 1 - i))
            for j in l[cur]:
                if j + 2 > i:
                    break
                mid = total - cur * (1 << (length - j - 1)) - cur
                mid >>= (length - i)
                if mid == cur:
                    return [j, i] if flag else [j + zero - 3, i + zero - 3]
                if mid < cur:
                    break
        return [-1, -1]

    """
    Key point:
        Those three parts should have same number of '1'. 
        and each one has total//3 . 
        we can find the very first '1' for each part and compare those three parts 
    """
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total, length = sum(arr), len(arr)
        if total == 0:
            return [0, length - 1]
        if total % 3:
            return [-1, -1]
        v = total // 3
        l, m, r = -1, -1, -1
        count = 0
        for i, n in enumerate(arr):
            if n == 0:
                continue
            count += 1
            if count == 1 and l < 0:
                l = i
            if count == v + 1 and m < 0:
                m = i
            if count == v * 2 + 1 and r < 0:
                r = i
                break
        n = len(arr[r:])
        if arr[l:l+n] == arr[m:m+n] == arr[r:]:
            return [l + n - 1, m + n]
        return [-1, -1]