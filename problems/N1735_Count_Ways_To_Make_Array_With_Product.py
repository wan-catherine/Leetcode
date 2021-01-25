import math

"""
First : need to remember how to create combination number !!! TEMPLATES CODE !!!

Second: when to get all factors about some numbers , remember use math.sqrt.

Third : C(n,a) == C(n, n-a)

About this problem:
for one query : [n, k]:
    1. find the count of all prime numbers of k
    2. for each prime number , use the Stars and Bars method to get all ways of the combination. 
        here we need to seperate into n groups, and all those groups actually allow empty (here we can think it's 1 ) 
         if it doesn't allow empty group then the ways : C(count, n-1) 
         if it allows empty group then we can add the number of groups into the count : C(count+n, n-1)
         
         
"""
class Solution(object):
    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        maxnum = max(max(u, v) for u, v in queries) + 15

        comb = [[0] * 15 for _ in range(maxnum)]
        module = 10 ** 9 + 7
        for i in range(maxnum):
            comb[i][0] = 1
            for j in range(1, 15):
                comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]

        def get_factors_count(num):
            mapping = {}
            up = int(math.sqrt(num)) + 1
            for i in range(2, up + 1):
                times = 0
                while not num % i:
                    times += 1
                    num //= i
                if times > 0:
                    mapping[i] = times
            if num != 1:
                mapping[num] = 1
            return mapping

        res = []
        for n, k in queries:
            ans = 1
            for count in get_factors_count(k).values():
                ans = ans * comb[n + count - 1][count] % module
            res.append(ans)
        return res

        # res = []
        # for n, k in queries:
        #     ans = 1
        #     num = k
        #     for x in range(2, k + 1):
        #         count = 0
        #         while not num % x:
        #             count += 1
        #             num //= x
        #         ans = ans * comb[n + count - 1][count] % module
        #     res.append(ans)
        # return res


