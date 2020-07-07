class Solution(object):
    def maxWidthRamp_timeout(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        res = 0
        for right in range(length-1,0,-1):
            left = 0
            while A[left] > A[right] and left <= right:
                left += 1
            if left <= right and A[left] <= A[right]:
                res = max(res, right - left)
        return res

    def maxWidthRamp_two_arrays(self, A):
        length = len(A)
        min_stack = [A[0]]*length
        max_stack = [A[-1]]*length
        for i in range(0,length):
            min_stack[i] = min(min_stack[i-1], A[i])
        for i in range(length-2, -1, -1):
            max_stack[i] = max(max_stack[i+1], A[i])

        res = 0
        left, right = 0, 0
        while right < length:
            if min_stack[left] <= max_stack[right]:
                res = max(res, right - left)
                right += 1
            else:
                left += 1
        return res

    def maxWidthRamp(self, A):
        length = len(A)
        stack = []
        for i in range(length):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
        res = 0
        for i in range(length-1, -1, -1):
            while stack and A[i] >= A[stack[-1]]:
                res = max(res, i - stack[-1])
                stack.pop()
        return res


