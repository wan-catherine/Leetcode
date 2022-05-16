import bisect
import heapq
from typing import List

"Not solved "

class Solution:
    def longestRepeating_(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        length = len(queryCharacters)
        s = list(s)
        for ii in range(length):
            s[queryIndices[ii]] = queryCharacters[ii]
            intervals = []
            ls = len(s)
            prev = 0
            for i in range(len(s)):
                if i == ls - 1 or s[i] != s[i + 1]:
                    intervals.append([prev, i])
                    prev = i + 1
            if ii == 16:
                print(intervals)
                print(''.join(s))

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s = list(s)
        intervals = []
        ls, length = len(s), len(queryCharacters)
        prev = 0
        res, pq = [], []
        for i in range(ls):
            if i == ls - 1 or s[i] != s[i+1]:
                intervals.append([prev, i])
                bisect.insort_left(pq, i - prev + 1)
                prev = i + 1

        def dele(n):
            index = bisect.bisect_left(pq, n)
            pq.pop(index)

        def insert(index, c):
            i = bisect.bisect_left(intervals, [index, index])
            if i == len(intervals) or intervals[i][0] > index:
                i -= 1
            a, b = intervals[i]
            s[index] = c
            dele(b - a + 1)
            if a == b:
                intervals[i] = [index, index]
                bisect.insort_left(pq, 1)
            elif a == index:
                intervals[i:i+1] = [[index, index], [index+1, b]]
                bisect.insort_left(pq, 1)
                bisect.insort_left(pq, b - index )
            elif b == index:
                intervals[i:i+1] = [[a, index-1], [index, b]]
                bisect.insort_left(pq, index - a)
                bisect.insort_left(pq, b - index + 1)
            else:
                intervals[i:i+1] = [[a, index-1], [index, index], [index+1, b]]
                bisect.insort_left(pq, index - a)
                bisect.insort_left(pq, 1)
                bisect.insort_left(pq, b - index)
            return i

        def merge(idx, pq):
            right = idx + 1
            if right < len(intervals) and s[intervals[right][0]] == s[intervals[idx][1]]:
                dele(intervals[idx][1] - intervals[idx][0] + 1)
                dele(intervals[right][1] - intervals[right][0] + 1)
                bisect.insort_left(pq, intervals[right][1] - intervals[idx][0] + 1)
                intervals[idx:idx + 2] = [[intervals[idx][0], intervals[right][1]]]
            left = idx - 1
            if left >= 0 and s[intervals[left][1]] == s[intervals[idx][0]]:
                dele(intervals[idx][1] - intervals[idx][0] + 1)
                dele(intervals[left][1] - intervals[left][0] + 1)
                bisect.insort_left(pq, intervals[idx][1] - intervals[left][0] + 1)
                intervals[left:left + 2] = [[intervals[left][0], intervals[idx][1]]]

        for i in range(length):
            idx, chr = queryIndices[i], queryCharacters[i]
            if s[idx] != chr:
                itx = insert(idx, chr)
                merge(itx, pq)
            v = [[0, 4], [5, 6], [7, 14], [15, 17], [18, 24], [25, 26], [27, 33], [34, 36], [37, 40], [41, 43], [44, 57], [58, 64], [65, 65], [66, 66], [67, 82], [83, 85], [86, 92], [93, 96], [97, 97], [98, 101], [102, 109], [110, 115], [116, 118], [119, 120], [121, 125], [126, 129], [130, 130], [131, 133], [134, 138], [139, 144], [145, 147], [148, 153], [154, 154], [155, 156], [157, 157], [158, 163], [164, 170], [171, 173], [174, 175], [176, 176], [177, 179], [180, 186], [187, 190], [191, 192], [193, 195], [196, 201], [202, 208], [209, 216], [217, 220], [221, 228], [229, 232], [233, 234], [235, 242], [243, 249], [250, 252], [253, 259], [260, 260], [261, 266], [267, 267]]
            for j in range(len(v)):
                if i == 16 and intervals[j] != v[j]:
                    print(i, intervals[j], v[j])
            res.append(pq[-1])
        return res


