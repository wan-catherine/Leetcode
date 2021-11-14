from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def get_permutation():
            cards.sort()
            res = []
            visited = [0] * 4
            def dfs(cur):
                if len(cur) == 4:
                    res.append(cur[:])
                    return
                prev = None
                for i in range(4):
                    if visited[i]:
                        continue
                    if cards[i] == prev:
                        continue
                    visited[i] = 1
                    prev = cards[i]
                    cur.append(cards[i])
                    dfs(cur[:])
                    cur.pop()
                    visited[i] = 0
            dfs([])
            return res
        permutation = get_permutation()
        # print(permutation)

        def helper(arr):
            if len(arr) == 1:
                return set([float(arr[0])])
            ans = set()
            for i in range(1,len(arr)):
                left = helper(arr[:i])
                right = helper(arr[i:])
                for l in left:
                    for r in right:
                        for op in '+-/*':
                            if op == '+':
                                ans.add(l + r)
                            elif op == '-':
                                ans.add(l - r)
                            elif op == '/':
                                ans.add(l * r)
                            elif r != 0:
                                ans.add(l/r)
            return ans

        for li in permutation:
            vals = helper(li)
            for val in vals:
                if abs(val - 24) < 1e-6:
                    return True
        return False
