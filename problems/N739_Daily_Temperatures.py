class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        t_len = len(T)
        stack = []
        res = [0] * t_len

        for i in range(t_len-1, -1, -1):
            count = 1
            while stack:
                if stack[-1][0] > T[i]:
                    break
                else:
                    previous, num = stack.pop()
                    count += num
            # here we need to decide if it has a warmer future or not .
            # if stack is not empty, then it means , it has a warmer future
            # if stack is empty, it means there is no warmer future, set count = 0
            if not stack:
                count = 0
            res[i] = count
            stack.append((T[i],count))
        return res



