from typing import List


class Solution(object):
    def makesquare_before(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.length = len(nums)
        if self.length < 4:
            return False
        nums_sum = sum(nums)
        if nums_sum % 4 :
            return False
        nums.sort(reverse=True)
        if nums[0] > nums_sum//4:
            return False
        siders = [0]*4

        return self.dfs(0, siders, nums, nums_sum//4)

    def dfs(self, index, siders, nums, value):
        if index >= self.length:
            for i in siders:
                if i != value:
                    return False
            return True

        for i in range(4):
            if siders[i] + nums[index] > value:
                continue
            siders[i] += nums[index]
            if self.dfs(index + 1, siders, nums, value):
                return True
            siders[i] -= nums[index]
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort()
        total = sum(matchsticks)
        if total % 4:
            return False
        length = len(matchsticks)
        l = total // 4
        for s in matchsticks:
            if s > l:
                return False
        used = [0] * length
        def helper(cur, num):
            nonlocal l
            if num == 4:
                return True
            # reverse , make it so fast!!!
            for i in range(length-1, -1, -1):
                if used[i]:
                    continue
                if cur + matchsticks[i] > l:
                    break
                if cur + matchsticks[i] == l:
                    used[i] = 1
                    if helper(0, num + 1):
                        return True
                    used[i] = 0
                elif cur + matchsticks[i] < l:
                    used[i] = 1
                    if helper(cur + matchsticks[i], num):
                        return True
                    used[i] = 0
            return False
        return helper(0, 0)

