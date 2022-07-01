class Solution:
    def getPermutation_(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq = [i for i in range(1, n+1)]
        res = ""

        for i in range(n-1, -1, -1):
            num = self.getNum(i)
            for j in range(1, n+1):
                if k <= j*num:
                    k -= (j - 1) * num
                    break
            p = 0
            for q in range(len(seq)):
                if seq[q] != 0:
                    p += 1
                if p == j:
                    res += str(seq[q])
                    seq[q] = 0
                    break
        return res

    def getNum(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res

    """
    20200620
    Tried a lot of times, all failed. 
    The key point here is to find the first temp value. 
    This one can't use k, just related to the ith.
    """
    def getPermutation_(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        res = []
        for i in range(1, n + 1):
            temp = self.getNum(n-i)
            j = 0
            while (j + 1) * temp <= k:
                j += 1
            k -= temp * j
            if k > 0:
                res.append(nums[j])
                del nums[j]
            else:
                res.append(nums[j - 1])
                del nums[j - 1]

        return ''.join(res)

    """
    Here is a trick to make things easier. 
    k -= 1. 
    so k // count, it will get the right index(0-based). 
    For example: 
         for [5,5,5]. 
         9//5 = 1, 10//5 = 2 ==> k=10, the index is 1, k=11, the index is 2. 
         
        if we don't minor one , then it needs to check if k % 5 == 0. 
        k = 10 ==> k // 5 = 2, then it should get the index = 2 - 1 = 1 . 
        k = 11 ==> k // 5 = 2 , then it should get index = 2 (no need minor 1).
    """
    def getPermutation(self, n, k):
        def permutation_count(k):
            count = 1
            for i in range(1, k+1):
                count *= i
            return count
        k -= 1
        res = []
        nums = [i + 1 for i in range(n)]
        for i in range(1, n+1):
            count = permutation_count(n-i)
            index = k // count
            res.append(nums[index])
            del nums[index]
            k -= count * index
        return ''.join(map(str, res + nums))

    def getPermutation_20220701(self, n: int, k: int) -> str:
        status = [1] * (n + 1)
        for i in range(1, n + 1):
            status[i] = status[i - 1] * i
        visited = [0] * n

        def helper(cur, v):
            left = n - len(cur) - 1
            count = status[left]
            for i in range(n):
                if visited[i]:
                    continue
                if v > count:
                    v -= count
                else:
                    visited[i] = 1
                    cur.append(str(i + 1))
                    helper(cur, v)

        res = []
        helper(res, k)
        return ''.join(res)