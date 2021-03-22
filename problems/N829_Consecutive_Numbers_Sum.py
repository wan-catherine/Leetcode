import math
"""
sum(x, x+1, x+2, ... , x+m) == N
==> (2*N - m*(m+1))/(2*(m+1)) == x , x must be an positive integer. 
the range of m here is around : (2*N - m*(m+1))/(2*(m+1)) > 0 
==> m < math.sqrt(2*N)
"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ans = 0
        for i in range(int(math.sqrt(2*N))+1):
            val = (2*N - i*i -i)
            if val > 0 and val % (2*i + 2) == 0:
                ans += 1
        return ans

