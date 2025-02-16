from typing import List


class Solution:
    def constructDistancedSequence(self, n: int):
        res = [0] * n*2
        used = set()

        def dfs(index):
            nonlocal n
            if len(used) == n:
                return True

            for i in range(n, 0, -1):
                if i in used:
                    continue
                used.add(i)
                if i == 1:
                    res[index] = 1
                    j = 1
                    while j < 2 * n:
                        if res[j] == 0:
                            break
                        j +=1
                    if dfs(j):
                        return True
                    res[index] = 0
                else:
                    if index + i < 2*n and res[index + i] == 0:
                        res[index] = i
                        res[index + i] = i
                        j = 1
                        while j < 2*n:
                            if res[j] == 0:
                                break
                            j += 1
                        if dfs(j):
                            return True
                        res[index] = 0
                        res[index+i] = 0
                used.remove(i)

        dfs(1)
        return res[1:]

    def constructDistancedSequence(self, n: int) -> List[int]:
        used = [0] * (n + 1)
        res = [0] * (2 * n - 1)

        def dfs(index):
            if index == 2 * n - 1:
                return True

            if res[index] != 0:
                return dfs(index + 1)

            for i in range(n, 0, -1):
                if used[i] == 1:
                    continue
                if i > 1 and ((index + i) >= 2 * n - 1 or res[index + i]) != 0:
                    continue

                used[i] = 1
                res[index] = i
                if i > 1:
                    res[index + i] = i

                if dfs(index + 1):
                    return True

                used[i] = 0
                res[index] = 0
                if i > 1:
                    res[index + i] = 0
            return False

        dfs(0)
        return res

