import collections
import math

class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.parents = list(range(100000+1))
        self.sizes = [1] * 100001
        primes = self.get_primes(int(math.sqrt(100000)))
        for num in A:
            val = num
            for p in primes:
                if p > val:
                    break
                if num%p:
                    continue
                if self.find(p) != self.find(num):
                    self.union(p, num)
                while not val % p :
                    val //= p

            if val > 1 and num != val:
                self.union(num, val)

        groups = collections.defaultdict(int)
        mapping = collections.defaultdict(set)
        for i in A:
            groups[self.find(i)] += 1
            mapping[self.find(i)].add(i)
        print(mapping[2])
        res = 0
        for key, val in groups.items():
            res = max(res, val)
        return res

    def find(self, a):
        # while self.parents[a] != a:
        #     self.parents[a] = self.parents[self.parents[a]]
        #     a = self.parents[a]
        # return a
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        a_p = self.find(a)
        b_p = self.find(b)
        if a_p == b_p:
            return

        if self.sizes[a_p] < self.sizes[b_p]:
            self.parents[a_p] = b_p
            self.sizes[b_p] += self.sizes[a_p]
        else:
            self.parents[b_p] = a_p
            self.sizes[a_p] += self.sizes[b_p]

    """
    Any natural number can be expressed as several primes multiplied.
    N = a*b*c*...*y (a < b < ... < y)
    The largest prime of a natural number is int(math.sqrt(N)).
    If y == int(math.squrt(N)) is not the largest , then there is x > y ==> x*y > N.So y is the largest prime .

    How to create prime?
    Find the first prime, then remove all numbers which n%prime == 0.
    """
    def get_primes(self, n):
        arr = [True] * n
        primes = []
        for i in range(2, n):
            if not arr[i]:
                continue
            primes.append(i)
            # here j can starts as i*i, better than 2*i. Let's say i = 5, we can direct consider 25 .
            # because 2*5,3*5,4*5 all ready be solved by i = [2,3,4]
            for j in range(i*i,n,i):
                arr[j] = False
        return primes


    def largestComponentSize_dict(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
        self.parents = collections.defaultdict(int)
        self.sizes = collections.defaultdict(int)
        for p in primes:
            self.parents[p] = p
            self.sizes[p] = 1
        for i in A:
            self.parents[i] = i
            self.sizes[p] = 1

        for num in A:
            val = num
            for p in primes:
                if p > num:
                    break
                if num % p:
                    continue
                if self.find(p) != self.find(num):
                    self.union(p, num)
                while not val % p:
                    val //= p
            if val > 1 and val != num:
                # we need to check this , because val maybe not show before. If we don't add this check, then all non-showed number's parent will be same as 0.
                if val not in self.parents:
                    self.parents[val] = val
                self.union(num, val)
        groups = collections.defaultdict(int)
        mapping = collections.defaultdict(set)
        for i in A:
            groups[self.find(i)] += 1
            mapping[self.find(i)].add(i)
        print(mapping[2])
        res = 0
        for _, val in groups.items():
            res = max(res, val)
        return res

    def union_dict(self, a, b):
        a_p = self.find(a)
        b_p = self.find(b)
        if a_p == b_p:
            return
        if self.sizes[a_p] < self.sizes[b_p]:
            self.parents[a_p] = b_p
            self.sizes[b_p] += self.sizes[a_p]
        else:
            self.parents[b_p] = a_p
            self.sizes[a_p] += self.sizes[b_p]

    def find_dict(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]