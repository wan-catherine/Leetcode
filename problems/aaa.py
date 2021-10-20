import bisect
import collections
import heapq
from typing import List


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        length = len(s)
        def check(i, j, count):
            # print(i, j)
            if count > 1:
                return False
            if i >= length or j < 0:
                return False
            if i >= j:
                return True
            if s[i] == s[j]:
                return check(i+1, j-1, count)
            else:
                if check(i+1, j, count + 1):
                    return True
                return check(i, j-1, count + 1)
        return check(0, length-1, 0)

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        stack = [(0, 1)]
        first, second = None, None
        visited = set()
        while stack:
            num, node = heapq.heappop(stack)
            if node == n:
                if not first:
                    first = num
                elif not second or second == first:
                    second = num
                else:
                    break
            for nxt in graph[node]:
                if (nxt, node) in visited:
                    continue
                visited.add((node, nxt))
                heapq.heappush(stack, (num+1, nxt))
        res = 0
        flag = 'Green'

        while second:
            if flag == 'Green':
                res += time
                t = res // change
                if t % 2:
                    flag = 'Red'
                second -= 1
            else:
                t = res % change
                res += change - t
                flag = 'Green'
        return res

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        count = collections.defaultdict(int)
        for u, v in tickets:
            bisect.insort_left(graph[u], v)
            count[(u, v)] += 1
        length = len(tickets)

        def dfs(node, cur):
            cur.append(node)
            if len(cur) == length + 1:
                return True, cur
            for nxt in graph[node]:
                if count[(node, nxt)] > 0:
                    count[(node, nxt)] -= 1
                    f, ans = dfs(nxt, cur[:])
                    if f:
                        return f, ans
                    count[(node, nxt)] += 1
            return False, None
        _, res = dfs('JFK', [])
        return res

    def verifyPreorder(self, preorder: List[int]) -> bool:
        length = len(preorder)
        def check(l, r):
            s, e = l, r
            if l >= r:
                return True
            root = preorder[l]
            l = l + 1
            while l < r:
                if preorder[l] < root:
                    l += 1
                    continue
                if preorder[r] > root:
                    r -= 1
                    continue
                return False
            return check(s + 1, l) and check(l, e)

        return check(0, length - 1)

if __name__ == '__main__':
    solution = Solution()
    # print(solution.secondMinimum())
    print(solution.verifyPreorder([4,2,3,1]))