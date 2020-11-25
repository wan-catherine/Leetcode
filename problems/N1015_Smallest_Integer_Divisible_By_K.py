class Solution(object):
    """
    num = a*K + r ==> num%K == r%K
    num_1 = num*10 + 1 = 10*a*K + 10*r + 1 ==> num_1%K == (10*r + 1)%K

    so for all num, num%K == (10*(last r) + 1)%K

    r = num%K ==> r < K
    so the while at most run K times, then :
        1. it find num which num%K == 0
        2. there is a cycle of r , we use used to check.

    """
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        n = 1
        res = 1
        used = set()
        while True:
            r = n % K
            if not r:
                return res
            if r in used:
                return -1
            used.add(r)
            n = 10*r + 1
            res += 1

    """
    Here we check K % 2 and K % 5 , then all other will be divisible. 
    we have 1, 2, ..., k-3, k-2, k-1 remainder.
    now if the num isn't divisible, it means ri, rj in those remainders are equal ==>
    (10*ri + 1)%K == (10*rj + 1)%K
    10*ri + 1 + a*K = 10*rj + 1
    (rj-ri) = a*K/10  ==> 0 < a < 10
    if K%2== 0 or K%5 == 0 , a can be 5 or 2, then rj can be same as ri.
    so it won't be divisible. 
    """
    def smallestRepunitDivByK_(self, K):
        if K % 2 == 0 or K % 5 == 0:
            return -1
        n = 1
        res = 1
        while True:
            r = n % K
            if not r:
                return res
            n = 10*r + 1
            res += 1

