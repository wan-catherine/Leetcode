"""
Very classical problem!!!

First, we need to move 1's into a k-length group, so it will be move the consecutive 1's.
So we will get a new array which only contains 1's index . Then it will be a sliding window problem.
We need to find a window which length is k and its sum(dist) is minimum.

Here it will be similar as problem : 296. Best Meeting Point.
We have :
    [p1, p2, p3, .... , pk] == > [q1, q2, q3, .... , qk] which is consecutive
We know the minimum distance will be we move all p* to it's medium p[k//2] (works both for even and odd).
so the distance = sum(abs(pi - p[k//2])) for i in range(1,k)

Then we can calculate all k-length window's distance and the miniumum one will be the result.
But here we use O(K) to get the distance , and 1 <= nums.length <= 10**5, 1 <= k <= sum(nums)
It will be O(N**2), so we need to optimize it .

Notice :
           0              k//2
   sum1 :  x   x   x   x   o   x   x   x   x
   sum2        x   x   x   x   o   x   x   x   x

1. - (arr[k//2] - arr[0])
2. + (arr[k//2 + 1] - arr[k//2]) * (k//2)
3. - (arr[k//2 + 1] - arr[k//2]) * (k - 1 - k//2)
4. + arr[k+1] - arr[k//2 + 1]

At this time, we get the minimum steps to move all 1's to the k//2 position.
But this problem asks us to move into a group, so we need to subtract by duplicated steps(left and right).

"""
class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = []
        for i, n in enumerate(nums):
            if n:
                arr.append(i)
        length = len(arr)
        mid = k//2
        dist = 0
        for i in range(k):
            dist += abs(arr[i] - arr[mid])
        res = dist
        for i in range(1, length-k+1):
            dist -= abs(arr[mid] - arr[i-1])
            dist += (arr[mid+1] - arr[mid]) * (k//2)
            dist -= (arr[mid+1] - arr[mid]) * (k-1-k//2)
            dist += arr[k+i-1] - arr[mid+1]
            mid += 1
            res = min(res, dist)
        for i in range(k//2):
            res -= i + 1
        for i in range(k//2+1,k):
            res -= i - k//2
        return res
