from typing import List


class Solution(object):
    def canPartitionKSubsets_dfs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum_nums = sum(nums)
        if sum_nums % k :
            return False
        self.target = sum_nums // k
        self.length = len(nums)
        self.visited = [0] * self.length
        return self.dfs(0, sorted(nums, reverse=True), k, 0)

    def dfs(self, index, nums, k, current):
        if k == 1:
            return True

        if current == self.target:
            k -= 1
            return self.dfs(0, nums, k, 0)

        for i in range(index, self.length):
            if current + nums[i] > self.target or self.visited[i]:
                continue
            self.visited[i] = 1
            if self.dfs(i + 1, nums, k, current + nums[i]):
                return True
            self.visited[i] = 0
        return False

    def canPartitionKSubsets_tle(self, nums, k):
        sum_nums = sum(nums)
        if sum_nums % k:
            return False
        targets = [sum_nums // k] * k
        length = len(nums)
        nums.sort(reverse=True)
        def dfs(index):
            if index == length:
                return True
            for i in range(k):
                if targets[i] - nums[index] >= 0:
                    targets[i] -= nums[index]
                    if dfs(index+1):
                        return True
                    targets[i] += nums[index]
            return False
        return dfs(0)

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        val = total // k

        nums.sort(reverse=True)
        length = len(nums)
        visited = [0] * length

        memo = set()

        def dfs(cur, t):
            if (cur, t, tuple(visited)) in memo:
                return False
            if cur == 0 and t == k:
                return True
            if cur > val:
                return False

            for i in range(length):
                if visited[i]:
                    continue
                if cur + nums[i] > val:
                    continue
                visited[i] = 1
                if cur + nums[i] == val:
                    if dfs(0, t + 1):
                        return True
                else:
                    if dfs(cur + nums[i], t):
                        return True
                visited[i] = 0
            memo.add((cur, t, tuple(visited)))
            return False

        return dfs(0, 0)





