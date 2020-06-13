"""
DFS
from N to 1 will be more efficient .
becausre position i = 1 can hold any number
"""
class Solution(object):
    def countArrangement(self, N):
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



