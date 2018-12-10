import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        arr = [1] * n
        arr[0] = 0
        arr[1] = 0
        end = int(math.sqrt(n)) + 1
        for i in range(2,end):
            if arr[i] == 0:
                continue
            if self.isPrime(i):
                self.SetZero(arr, i)
        return sum(arr)


    def SetZero(self, arr, num):
        j = 2
        while j * num < len(arr):
            arr[j * num] = 0
            j += 1



    def isPrime(self, num):
        i = 2
        while i < num/2:
            if num % i == 0:
                return False
            i += 1
        return True