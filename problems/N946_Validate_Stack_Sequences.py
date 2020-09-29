class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if not pushed:
            return True
        stack = []
        index = 0
        for v in pushed:
            stack.append(v)
            while stack and stack[-1] == popped[index]:
                index += 1
                stack.pop()
        if stack:
            return False
        return True
