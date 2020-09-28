class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if not asteroids:
            return []
        stack = []
        for i in asteroids:
            if not stack:
                stack.append(i)
                continue
            if stack[-1] < 0:
                stack.append(i)
            else:
                if i > 0:
                    stack.append(i)
                else:
                    while stack and stack[-1] > 0 and i + stack[-1] < 0:
                        stack.pop()
                    if stack and stack[-1] + i == 0:
                        stack.pop()
                    elif not stack or (stack and stack[-1] < 0):
                        stack.append(i)
        return stack

