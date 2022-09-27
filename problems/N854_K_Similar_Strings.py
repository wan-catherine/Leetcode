class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        length = len(s1)
        stack = [s1]
        step = 0
        visited = set()
        while stack:
            nstack = []
            for s in stack:
                idx = -1
                for i in range(length):
                    if s[i] == s2[i]:
                        continue
                    else:
                        idx = i
                        break
                if idx < 0:
                    continue
                for i in range(1, length):
                    # we need to do greedy choice here to avoid TLE
                    if s[i] != s2[idx]:
                        continue
                    li = list(s)
                    li[idx], li[i] = li[i], li[idx]
                    ns = ''.join(li)
                    if ns == s2:
                        return step + 1
                    if ns in visited:
                        continue
                    visited.add(ns)
                    nstack.append(ns)
            stack = nstack
            if stack:
                step += 1
        return step