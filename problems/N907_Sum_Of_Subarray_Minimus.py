class Solution(object):
    # time complexsity is o(n**2), timeout
    def sumSubarrayMins_timeout(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        mod = 10 ** 9 + 7
        a_len = len(A)
        for i in range(a_len):
            min = A[i]
            for j in A[i:]:
                if min > j:
                    min = j
                res += min
        return res % mod

    # explaination : https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
    # for one number a, all sub-arrays which the minute is a.
    # left[a] means the count of numbers which on the left of a and all >= a
    # right[a] means the count of numbers which on the right of a and all > a
    # sum = left[a] * right[a] * a
    # here need to notice about the duplicated number , so we choose strict less and un-strict less.
    # order doesn't matter

    def sumSubarrayMins_other(self, A):
        a_len, mod = len(A), 10 ** 9 + 7
        left, right = [0] * a_len, [0] * a_len
        temp = []

        for i in range(a_len):
            count = 1
            while temp:
                if temp[-1][0] >= A[i]:
                    count += temp.pop()[1]
                else:
                    break
            left[i] = count
            temp.append((A[i], count))
        temp = []
        for i in range(a_len-1, -1, -1):
            count = 1
            while temp:
                if temp[-1][0] > A[i]:
                    count += temp.pop()[1]
                else:
                    break
            right[i] = count
            temp.append((A[i], count))
        print(left)
        print(right)
        return sum(a*l*r for a, l, r in zip(A, left, right)) % mod

    # don't understand :(
    # non-decreasing stack
    def sumSubarrayMins(self, A):
        res = 0
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                print(i-j)
                print(j-k)
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10 ** 9 + 7)
