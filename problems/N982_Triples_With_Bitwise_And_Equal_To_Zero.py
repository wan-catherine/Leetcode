import collections
from typing import List


class Solution:
    def countTriplets_brute_force(self, A: List[int]) -> int:
        mapping = collections.defaultdict(int)
        length = len(A)
        for i in range(length):
            for j in range(length):
                mapping[A[i] & A[j]] += 1
        ans = 0
        for num in A:
            for key in mapping:
                if num & key == 0:
                    ans += mapping[key]
        return ans

    def countTriplets(self, A: List[int]) -> int:
        mapping = collections.defaultdict(int)
        length = len(A)
        for i in range(length):
            for j in range(length):
                mapping[A[i]&A[j]] += 1

        ans = 0
        N = (1 << 16)
        for num in A:
            val = N - 1 - num  # get the number : 1 -> 0, 0 -> 1
            v = val
            # get all the subset of the v which the bit it '1'
            while v:
                if v in mapping:
                    ans += mapping[v]
                v = (v-1) & val
            ans += mapping[0]
        return ans