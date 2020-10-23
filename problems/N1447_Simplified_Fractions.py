class Solution(object):
    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return []

        arr = []
        for i in range(n+1):
            temp = [1]*(i+1)
            arr.append(temp)

        res = []
        for i in range(2, n+1):
            for j in range(1, i):
                if arr[i][j] == 1:
                    res.append(f"{j}/{i}")
                    k = 2
                    while i * k <= n:
                        arr[i*k][j*k] = 0
                        k += 1
        return res