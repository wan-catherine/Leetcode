class Solution(object):
    def lastRemaining_TLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(arr, flag):
            length = len(arr)
            if length == 1:
                return arr[0]
            res = []

            if flag:
                for i in range(1, length, 2):
                    res.append(arr[i])
            else:
                if length % 2:
                    for i in range(1, length, 2):
                        res.append(arr[i])
                else:
                    for i in range(0, length, 2):
                        res.append(arr[i])
            return helper(res, not flag)
        return helper([i for i in range(1, n+1)], True)

    """
    Time complexity : O(nlgn)
    Notice : 
        1. use head to record the res. There are two situations need to update head
            a. when remove from left 
            b. when remove from right and the n % 2 == 1 (it same as remove form right) 
                2,4,6,8,10 ==> 4, 6
        2. use step to record the next number     
    """
    def lastRemaining(self, n):
        left = True
        step = 1
        head = 1
        while n > 1:
            if left or n % 2:
                head += step
            n //= 2
            step *= 2
            left = not left
        return head
