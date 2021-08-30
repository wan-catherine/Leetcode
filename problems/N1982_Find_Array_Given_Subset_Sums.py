import bisect
from collections import deque
from typing import List, Counter

"""
find the largest and second largest number in sums. 
f, s = largest, second largest. 
f - s = diff

NNNNPPPPPP
There are two situations: 
1. diff == the smallest positive number
2. diff == the largest negative number 

Then we need to consider those two ways. 

When we have the diff, then the KEY POINT is to split the snums into two array which both have len(sums)//2 numbers. 
arr1 = xxxx which contains the diff
arr2 = yyyy which doesn't contain the diff. 

The recursive by setting snums = arr2. 

"""
class Solution:
    def recoverArray_TLE(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        def dfs(arr, cur, sarr):
            ll = len(arr)
            arr_copy = list(arr)
            if ll == 2:
                if arr[0] == 0 or arr[1] == 0:
                    cur.append(arr[0] if arr[0] != 0 else arr[1])
                    return cur[:]
                return []
            ans = deque()
            sans = set()
            first, second = arr[-1], arr[-2]
            diff = first - second
            index = bisect.bisect_left(arr, diff)

            if index < ll and arr[index] == diff:
                while arr:
                    f = arr.pop()
                    s = f - diff
                    if s not in sarr:
                        break
                    ans.appendleft(s)
                    sans.add(s)
                    arr.remove(s)
                if len(ans) == ll // 2:
                    cur.append(diff)
                    arrres = dfs(ans, cur[:], sans)
                    if len(arrres) == n:
                        return arrres
                cur.pop()
            arr = arr_copy
            ans, sans = [], set()
            first, second = arr[0], arr[1]
            diff = first - second
            index = bisect.bisect_left(arr, diff)
            if index < ll and arr[index] == diff:
                while arr:
                    f = arr[0]
                    arr = arr[1:]
                    s = f - diff
                    if s not in sarr:
                        break
                    ans.append(s)
                    sans.add(s)
                    arr.remove(s)
            cur.append(diff)
            if len(ans) != ll // 2:
                return []
            arrres = dfs(ans, cur[:], sans)
            if len(arrres) == n:
                return arrres
            return []

        res = dfs(sums, [], set(sums))
        return res

    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums = sorted(sums, reverse=True)
        ans = []

        def remove(sumset, ele):
            if sumset[ele] > 1:
                sumset[ele] -= 1
            else:
                del sumset[ele]

        while len(sums) > 2:
            array1, array2 = [], []
            num = sums[0] - sums[1]
            sumset = Counter(sums)
            for ele in sums:
                if ele in sumset:
                    array2.append(ele)
                    array1.append(ele - num)
                    remove(sumset, ele)
                    remove(sumset, ele - num)
            if num in array2:
                idx = array2.index(num)
                if array1[idx] == 0:
                    ans.append(num)
                    sums = array1
                    continue
            ans.append(-1 * num)
            sums = array2

        return ans + [sums[1]] if sums[0] == 0 else ans + [sums[0]]

