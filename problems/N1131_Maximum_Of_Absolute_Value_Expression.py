"""
https://github.com/wisdompeak/LeetCode/tree/master/Math/1131.Maximum-of-Absolute-Value-Expression
Manhattan distance for 3-D

Let's see Manhattan distance for 2-D
M_d( (a1, b1), (a2, b2) ) = |a1-a2| + |b1-b2|
= max {
    (a1-a2) + (b1-b2),
    (a1-a2) + (b2-b1),
    (a2-a1) + (b1-b2),
    (a2-a1) + (b2-b1)
}
= max {
    (a1+b1) - (a2+b2),
    (a1-b1) - (a2-b2),
    (-a1+b1) - (-a2+b2),
    (-a1-b1) - (-a2-b2)
}

then to any i, j :
max |ai−aj|+|bi−bj|= max over (i,j){
  max {
      (ai+bi)−(aj+bj)，
      (ai−bi)−(aj−bj)，
      (−ai+bi)−(−aj+bj)，
      (−ai−bi)−(−aj−bj) }
}

we change the two max order :
 max{
    max over (i,j)  {(ai+bi)−(aj+bj)},
    max over (i,j)  {(ai−bi)−(aj−bj)},
    max over (i,j)  {(−ai+bi)−(−aj+bj)},
    max over (i,j)  {(−ai−bi)−(−aj−bj)},
 }

then for first of four of them :
    max over (i,j)  {(ai+bi)−(aj+bj)}
    =   (max {ak+bk} for any k)  - (min {ak+bk} for any k)

This is for 2-D, it's [[1,1], [1,-1], [-1,1], [-1,-1]]
For 3-D,it has 8 possiblity (2**3) , each number has two status (1, -1) : 000 ~ 111.

"""
import sys


class Solution(object):
    def maxAbsValExpr_1(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        d = [[1,1], [1,-1], [-1,1], [-1,-1]]
        res, length = 0, len(arr1)

        for i, j in d:
            minimum = i * arr1[0] + j * arr2[0] + 0
            for index in range(length):
                current = i * arr1[index] + j * arr2[index] + index
                res = max(res, current - minimum)
                minimum = min(minimum, current)
        return res

    def maxAbsValExpr_2(self, arr1, arr2):
        n = len(arr1)
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for i in range(n):
            l1.append(arr1[i] + arr2[i] + i)
            l2.append(-arr1[i] + arr2[i] + i)
            l3.append(arr1[i] - arr2[i] + i)
            l4.append(-arr1[i] - arr2[i] + i)
        maxAbsVal = max(l1) - min(l1)
        maxAbsVal = max(maxAbsVal, max(l2) - min(l2))
        maxAbsVal = max(maxAbsVal, max(l3) - min(l3))
        maxAbsVal = max(maxAbsVal, max(l4) - min(l4))
        return maxAbsVal

    def maxAbsValExpr(self, arr1, arr2):
        length = len(arr1)
        arr = [[0]*3 for _ in range(length)]
        for i in range(length):
            arr[i][0] = arr1[i]
            arr[i][1] = arr2[i]
            arr[i][2] = i

        res = 0
        for i in range(8):
            mi, mx = sys.maxsize, -sys.maxsize
            for j in range(length):
                val = 0
                for k in range(3):
                    if ((1<<k) & i):
                        val += arr[j][k]
                    else:
                        val -= arr[j][k]
                mi = min(mi, val)
                mx = max(mx, val)
            res = max(res, mx-mi)
        return res
