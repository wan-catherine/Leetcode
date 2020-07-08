import collections


class Solution(object):
    def minDominoRotations_myself(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        length = len(A)
        dict_a = collections.defaultdict(set)
        dict_b = collections.defaultdict(set)

        for i in range(length):
            dict_a[A[i]].add(i)
            dict_b[B[i]].add(i)

        res = length
        for i in range(1, 7):
            if i in dict_a:
                b_index = set()
                for key in dict_a:
                    if key == i:
                        continue
                    b_index = b_index.union(dict_a[key])
                diff = b_index.difference(dict_b[i])
                if diff:
                    continue
                res = min(res, len(b_index))

            if i in dict_b:
                a_index = set()
                for key in dict_b:
                    if key == i:
                        continue
                    a_index = a_index.union(dict_b[key])
                diff = a_index.difference(dict_a[i])
                if diff:
                    continue
                return min(res, len(a_index))

        return  res if res < length else -1

    """
    Count the occurrence of all numbers in A and B,
    and also the number of domino with two same numbers.
    
    Try all possibilities from 1 to 6.
    If we can make number i in a whole row,
    it should satisfy that countA[i] + countB[i] - same[i] = n
    
    Take example of
    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]
    
    countA[2] = 4, as A[0] = A[2] = A[4] = A[5] = 2
    countB[2] = 3, as B[1] = B[3] = B[5] = 2
    same[2] = 1, as A[5] = B[5] = 2
    
    We have countA[2] + countB[2] - same[2] = 6,
    so we can make 2 in a whole row.
    
    Time O(N), Space O(1)
    """
    def minDominoRotations(self, A, B):
        length = len(A)
        count_a = [0] * 7
        count_b = [0] * 7
        same = [0] * 7
        for i in range(length):
            count_a[A[i]] += 1
            count_b[B[i]] += 1
            if A[i] == B[i]:
                same[A[i]] += 1

        res = length
        for i in range(1, 7):
            if count_a[i] + count_b[i] - same[i] == length:
                res = min(res, count_a[i] - same[i], count_b[i] - same[i])

        return res if res < length else -1
