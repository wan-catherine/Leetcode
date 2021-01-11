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
