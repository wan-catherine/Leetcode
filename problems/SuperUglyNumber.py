class Solution:
    def nthSuperUglyNumber_timeout(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 1 :
            return 1

        res = [1]
        number = 2
        while len(res) < n:
            temp = number
            for i in primes:
                if temp % i == 0:
                    temp = temp // i
                    while temp % i == 0:
                        temp = temp // i
                if temp == 1:
                    break
            if temp == 1:
                res.append(number)
            number += 1

        return res[-1]

    def nthSuperUglyNumber_timeout(self, n, primes):
        if n == 1:
            return 1

        l = len(primes)
        index = [0] * l
        res = [1]
        count = 1
        while count < n:
            temp = [primes[i] * res[index[i]] for i in range(l)]
            num = temp[0]
            p = 0
            for a in range(1,len(temp)):
                if num > temp[a]:
                    num = temp[a]
                    p = a
            index[p] += 1
            if num != res[-1]:
                res.append(num)
                count += 1

        return res[-1]

    def nthSuperUglyNumber(self, n, primes):
        import heapq
        k = len(primes)
        p = [1] * n
        idx = [0] * k
        fct = [0] * n

        pq = [(primes[i], i) for i in range(k)]
        heapq.heapify(pq)

        for m in range(1, n):
            p[m], i = heapq.heappop(pq)
            idx[i] += 1
            fct[m] = i
            while fct[idx[i]] > i:
                idx[i] += 1
            heapq.heappush(pq, (primes[i] * p[idx[i]], i))

        return p[-1]




