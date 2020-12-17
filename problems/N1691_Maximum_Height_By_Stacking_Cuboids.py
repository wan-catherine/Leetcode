class Solution(object):
    """
    This actually an LIS (longes increasing subsequences) DP problem.
    We can can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.
    In order to solve this, we can permute the width, length and height. 3! = 6.
    There might be duplicated for those 6 situations, but we can only include only one of them .
    So we input the fouth : index.
    And sort the [l, w, h, i].
    """
    def maxHeight_(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        cubs = []
        for i, li in enumerate(cuboids):
            l,w,h = li[0], li[1], li[2]
            cubs.append([l, w, h, i])
            cubs.append([w, l, h, i])
            cubs.append([w, h, l, i])
            cubs.append([l, h, w, i])
            cubs.append([h, l, w, i])
            cubs.append([h, w, l, i])

        cubs.sort()
        length = len(cubs)
        cubs = [[0,0,0,-1]] + cubs

        dp = [0]*(length+1)

        res = 0
        for i in range(1, length+1):
            dp[i] = cubs[i][0]
            for j in range(1, i):
                if cubs[j][0] <= cubs[i][0] and cubs[j][1] <= cubs[i][1] and cubs[j][2] <= cubs[i][2] and cubs[j][3] != cubs[i][3]:
                    dp[i] = max(dp[i], dp[j] + cubs[i][0])

            res = max(res, dp[i])
        return res

    """
    We don't need to consider all 6 permutation . 
    We can only consider the largest height. 
    Think about : 
    A(a1, a2, a3) and B(b1, b2, b3). 
    if A can top of B ==>
        1. a1 <= b1
        2. a2 <= b2
        3. a3 <= b3
        
    ==>
        1. min(a1, a2, a3) <= min(b1, b2, b3)
        2. mid(a1, a2, a3) <= mid(b1, b2, b3)
        3. max(a1, a2, a3) <= max(b1, b2, b3)
        
    """
    def maxHeight(self, cuboids):
        cuboids = [[0,0,0]] + [sorted(li) for li in cuboids]
        cuboids.sort()
        length = len(cuboids)
        dp = [0]*length

        res = 0

        for i in range(1, length):
            dp[i] = cuboids[i][2]
            for j in range(1, i):
                if cuboids[j][0] <= cuboids[i][0] and cuboids[j][1] <= cuboids[i][1] and cuboids[j][2] <= cuboids[i][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
            res = max(res, dp[i])
        return res

