import collections
"""
All subarray sum we can think about prefix sum array. 
The here is the key point: 
For example : 
prefix 9 , prefix 4, the subarray between them is 5 . if k == 5, then this subarray will be one of the answer.
math proof : 
(prefix_i - prefix_j) % k == 0 
==> prefix_i % k - prefix_j % k == 0
==> prefix_i % k == prefix_j % k

"""
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return 0
        prefix_sum = A[:]
        length = len(A)
        for i in range(1,length):
            prefix_sum[i] += prefix_sum[i-1]

        remainder_count_mapping = collections.defaultdict(int)
        for i in range(length):
            remainder_count_mapping[prefix_sum[i] % K] += 1

        count = 0
        for key, value in remainder_count_mapping.items():
            count += value * (value-1) //2  #when value >= 2, it means we find prefix_i and prefix_j which satifise : (prefix_i - prefix_j) % k == 0 , permutation here .
            if key == 0:
                count += value  # when key == 0, it means each one of them can be a subarray 
        return count

