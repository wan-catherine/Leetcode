from typing import List


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        ls = len(s)
        left, right = ('#' + s[:ls//2], '#' + s[ls//2:][::-1])
        diff = [0] * (ls // 2 + 1)
        preleft, preright = [[0] * 26 for _ in range(ls // 2 + 1)], [[0] * 26 for _ in range(ls // 2 + 1)]
        for i in range(1, ls // 2 + 1):
            diff[i] = diff[i-1] + (1 if left[i] != right[i] else 0)
            for ch in range(26):
                preleft[i][ch] = preleft[i-1][ch] + (1 if ord(left[i]) - ord('a') == ch else 0)
                preright[i][ch] = preright[i-1][ch] + (1 if ord(right[i]) - ord('a') == ch else 0)

        def process(a, b, c, d):
            cross, left, right = [], [], []
            if max(a, c) <= min(b, d):
                cross.append((max(a, c), min(b, d)))
            if len(cross) == 0:
                left.append((a, b))
                right.append((c, d))
            else:
                if a <= c - 1:
                    left.append((a, c-1))
                if b >= d + 1:
                    left.append((d+1, b))
                if c <= a -1:
                    right.append((c, a-1))
                if d >= b + 1:
                    right.append((b+1, d))
            union = cross + left + right
            cd = 0
            for s, e in union:
                cd += diff[e] - diff[s - 1]
            if cd != diff[-1]:
                return False

            pab, pcd = [0] * 26, [0] * 26
            for i in range(26):
                pab[i] = preleft[b][i] - preleft[a-1][i]
                pcd[i] = preright[d][i] - preright[c-1][i]

            for i in range(26):
                for p, q in left:
                    pab[i] -= preright[q][i] - preright[p-1][i]
                for p, q in right:
                    pcd[i] -= preleft[q][i] - preleft[p-1][i]
                if pab[i] < 0 or pcd[i] < 0:
                    return False

            for i in range(26):
                if pab[i] != pcd[i]:
                    return False
            return True

        arr = []
        for p, q, k, v in queries:
            a, b = p + 1, q + 1
            c, d = ls - v, ls - k
            arr.append(process(a, b, c, d))

        return arr




