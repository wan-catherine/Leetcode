class Solution:
    def canPartition_timeout(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        dp = [0]
        flag = sum_nums / 2
        for num in nums:
            temp = dp[:]
            for i in temp:
                value = num + i
                if value == flag:
                    return True
                dp.append(value)
        return False

    def canPartition_two_array(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        dp = [1] + [0] * sum_nums
        for num in nums:
            temp = dp[:]
            for i in range(len(dp)):
                if temp[i]:
                    dp[i+num] = 1
            if dp[sum_nums//2]:
                return True
        return False

    def canPartition_before(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        dp = [1] + [0] * sum_nums
        for num in nums:
            for i in range(sum_nums, -1, -1):
                if dp[i]:
                    dp[i+num] = 1
            if dp[sum_nums//2]:
                return True
        return False

# d[i][j] : by using the first i nums, the totally sum is j, then it's doable or not
# d[i][j] has two situations :
#         1. not used the ith num : d[i-1][j]
#         2. used the ith num : d[i-1][j - nums[i-1]]
# d[i][j] = d[i-1][j] or d[i-1][j - nums[i-1]]
# Here because we can reuse the number in nums, so for the second situation, it's d[i-1] not
# d[i] (for 322, 518, it will be d[i], because the coins there is infinite)
# also need to check if j - nums[i-1] >= 0


    def canPartition_dp(self, nums):
        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        dp = [True] +[False] * sum_nums
        for i in range(1,len(nums)+1):
            before_dp = dp[:]
            for j in range(1, sum_nums+1):
                if j - nums[i-1] >= 0:
                    dp[j] = dp[j] or before_dp[j-nums[i-1]]
            if dp[sum_nums//2]:
                return True
        return False

    #20201127
    def canPartition_dfs_TLE(self, nums):
        total = sum(nums)
        if total % 2:
            return False
        length = len(nums)
        nums.sort(reverse=True)
        total //= 2
        visited = [False] * length
        def dfs(pos, cur):
            nonlocal total, length
            if cur == total:
                return True
            if cur > total:
                return False
            if pos == length:
                return False
            for i in range(pos, length):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False:
                    continue
                visited[i] = True
                if dfs(i+1, cur+nums[i]):
                    return True
                visited[i] = False
            return False

        return dfs(0, 0)

    """
    The key point is why we do this : for i in range(total,-1, -1) , instead of : for i in range(total + 1). 
    For this problem, the induction rule:

    If not picking nums[i - 1], then dp[i][j] = dp[i-1][j]
    if picking nums[i - 1], then dp[i][j] = dp[i - 1][j - nums[i - 1]]
    You can see that if you point them out in the matrix, it will be like:
    
                  j
        . . . . . . . . . . . . 
        . . . . . . . . . . . .  
        . . ? . . ? . . . . . .  ?(left): dp[i - 1][j - nums[i], ?(right): dp[i - 1][j]
    i	. . . . . # . . . . . .  # dp[i][j]
        . . . . . . . . . . . . 
        . . . . . . . . . . . . 
        . . . . . . . . . . . . 
        . . . . . . . . . . . . 
        . . . . . . . . . . . . 
    Optimize to O(2*n): you can see that dp[i][j] only depends on previous row, so you can optimize the space by only using 2 rows instead of the matrix. Let's say array1 and array2. Every time you finish updating array2, array1 have no value, you can copy array2 to array1 as the previous row of the next new row.
    Optimize to O(n): you can also see that, the column indices of dp[i - 1][j - nums[i] and dp[i - 1][j] are <= j. The conclusion you can get is: the elements of previous row whose column index is > j(i.e. dp[i - 1][j + 1 : n - 1]) will not affect the update of dp[i][j] since we will not touch them:
                  j
        . . . . . . . . . . . . 
        . . . . . . . . . . . .  
        . . ? . . ? x x x x x x  you will not touch x for dp[i][j]
    i	. . . . . # . . . . . .  # dp[i][j]
        . . . . . . . . . . . . 
        . . . . . . . . . . . . 
        . . . . . . . . . . . . 
        . . . . . . . . . . . . 
        . . . . . . . . . . . . 
    Thus if you merge array1 and array2 to a single array array, if you update array backwards, all dependencies are not touched!
    
        (n represents new value, i.e. updated)
        . . ? . . ? n n n n n n n
                  #  
    However if you update forwards, dp[j - nums[i - 1]] is updated already, you cannot use it:
    
        (n represents new value, i.e. updated)
        n n n n n ? . . . . . .  where another ? goes? Oops, it is overriden, we lost it :(
                  #  
    Conclusion:
    So the rule is that observe the positions of current element and its dependencies in the matrix. Mostly if current elements depends on the elements in previous row(most frequent case)/columns, you can optimize the space.
    """
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 :
            return False
        total //= 2
        dp = [False] * (total + 1)
        dp[0] = True

        for n in nums:
            for i in range(total,-1, -1):
                if i >= n and dp[i-n]:
                    dp[i] = True
        return dp[-1]

