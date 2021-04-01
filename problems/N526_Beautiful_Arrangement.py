"""
DFS
from N to 1 will be more efficient .
because position i = 1 can hold any number
"""
class Solution(object):
    def countArrangement_(self, N):
        """
        :type N: int
        :rtype: int
        """
        index_nums = [[] for i in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, N+1):
                if not i % j or not j % i:
                    index_nums[i].append(j)

        used = [0] * (N + 1)
        # return self.dfs(1, used, index_nums, N)
        return self.dfs_reverse(N, used, index_nums, N)

    def dfs_reverse(self, index, used, index_nums, N):
        if index == 1:
            for i in index_nums[index]:
                if not used[i]:
                    return 1
            return 0

        count = 0
        for i in index_nums[index]:
            if not used[i]:
                temp = used[:]
                temp[i] = 1
                count += self.dfs_reverse(index-1, temp, index_nums, N)
        print(f"{index}, {count}")
        return count

    def dfs(self, index, used, index_nums, N):
        if index > N:
            return 0
        if index == N:
            for i in index_nums[index]:
                if not used[i]:
                    return 1
            return 0
        count = 0
        for i in index_nums[index]:
            if not used[i]:
                temp = used[:]
                temp[i] = 1
                count += self.dfs(index+1, temp, index_nums, N)
        return count

    # update at 20210103
    def countArrangement(self, n: int) -> int:
        mapping = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if not j % i or not i % j:
                    mapping[i].append(j)
        visited = [0] * (n + 1)

        def dfs(index):
            if index == n:
                for num in mapping[n]:
                    if not visited[num]:
                        return 1
            count = 0
            for num in mapping[index]:
                if visited[num]:
                    continue
                visited[num] = 1
                count += dfs(index + 1)
                visited[num] = 0
            return count

        return dfs(1)

    # 20210331 update
    def countArrangement(self, n: int) -> int:
        memo = {}

        def dfs(index, state):
            nonlocal n
            if state == (1 << n) - 1:
                return 1
            if (index, state) in memo:
                return memo[(index, state)]
            ans = 0
            for i in range(1, n + 1):
                if state & (1 << i - 1):
                    continue
                if i % (index+1) == 0 or (index+1) % i == 0:
                    ans += dfs(index + 1, state | (1 << i - 1))
            memo[(index, state)] = ans
            return ans

        return dfs(0, 0)
