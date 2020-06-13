"""
we can have an array like this :
1   k+1  2   k  3   k-1  4  k-2
so the different |a[i] - a[i+1]| are : k, k-1, k-2......
so left are from k+2 ~ n, we can directly append to the result.

1,2,3,4,...x
k+1,k,k-1,k-2,...y
This is a point, |x-y| == 1

in order to have K distinct integers , we need to have k+1 in the array.
len(k+1, k-1,...) == (k+1)//2
x = (k+1)// 2 + (1 if k is even)

so when we append k + 2 to the result , |k+2 - last number(x or k- (k+1)//2 + 1)| < k,
so it's ok to append it .

after k+2 to n, the diff will always 1. so also ok .
"""
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = [1]
        count = 0
        start = 1
        for i in range(1,n):
            if i % 2:
                res.append(k + 1 - i // 2)
            else:
                start += 1
                res.append(start)
            count += 1
            if count == k:
                break
        for i in range(k+2, n+1):
            res.append(i)
        return res
