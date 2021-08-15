"""
Explanation and Proof
Assume: n = 2^p -1
We are given: [1, 2, 3, ....., n-3, n-2, n-1, n]
We can apply any number of bit swap operations between any pair of numbers
and we want to do it in such a way that minimizes the product of all the numbers.

For any two numbers, x and y, if x <= y then (x-1)*(y+1) = x*y + x - y - 1 < x*y
Using this, we can develop a greedy approach to reduce the given numbers to
[1, 1, 1, ... , n-1, n-1, n-1, n] where 1 and n-1 appear n/2 times.
These numbers will yield the least product since there is no way to make a pair
that gives a lower product without reducing one of the numbers to zero, which is not allowed.
"""

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        n = 2 ** p - 1
        M = 10**9 + 7
        return pow((n-1), n//2, M) * n % M