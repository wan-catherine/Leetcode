"""
    Any natural number can be expressed as several primes multiplied.
    N = a*b*c*...*y (a < b < ... < y)
    The largest prime of a natural number is int(math.sqrt(N)).
    If y == int(math.squrt(N)) is not the largest , then there is x > y ==> x*y > N.So y is the largest prime .

    How to create prime?
    Find the first prime, then remove all numbers which n%prime == 0.
"""
class Primes():
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
