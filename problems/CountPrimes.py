import math
class Solution:
    def countPrimes_(self, n):
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
                # print(i)
                self.SetZero(arr, i)
        return sum(arr)


    def SetZero(self, arr, num):
    #     # j = 2
    #     # while j * num < len(arr):
    #     #     arr[j * num] = 0
    #     #     j += 1
    #
    # def isPrime(self, num):
        i = 2
        while i < num/2:
            if num % i == 0:
                return False
            i += 1
        return True

    def countPrimes__(self, n):
        if n < 2:
            return 0
        end = int(math.sqrt(n))
        arr = [1] * n
        arr[0], arr[1] = 0, 0
        for i in range(2, end + 1):
            if not arr[i]:
                continue
            # python list operation is much faster than loop!!!
            arr[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)
            # j = 2
            # while j * i < n:
            #     arr[j * i] = 0
            #     j += 1
            # for j in range(i, n):
            #     num = j*i
            #     if num < n:
            #         arr[num] = 0
            #     else:
            #         break
        # print(arr)
        return sum(arr)

    def countPrimes(self, n):
        primes = []
        arr = [1] * n
        arr[0], arr[1] = 0, 0
        for i in range(2, n):
            if arr[i]:
                primes.append(i)
            for j in range(len(primes)):
                index = i * primes[j]
                if index >= n:
                    break
                arr[index] = 0
                if not i % primes[j]:
                    break
        return len(primes)

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        arr = [1] * n
        arr[0], arr[1] = 0, 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if not arr[i]:
                continue
            for j in range(i, n):
                index = i * j
                if index >= n:
                    break
                # print(index)
                arr[index] = 0
        return sum(arr)