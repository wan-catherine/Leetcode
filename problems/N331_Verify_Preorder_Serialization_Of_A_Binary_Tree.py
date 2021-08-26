class Solution(object):
    def isValidSerialization_myself(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        orders = preorder.split(',')
        stack = []
        flag = True
        for i in orders:
            if not stack:
                if not flag:
                    return False
                flag = False
                stack.append([i, 0])
                continue
            if i == '#':
                if stack[-1][0] == '#':
                    return False
                stack[-1][1] += 1
            else:
                stack.append([i, 0])
            while stack and stack[-1][1] == 2:
                stack.pop()
                if stack:
                    stack[-1][1] += 1
        if stack:
            for i in stack:
                if i[0] != '#':
                     return False
            return True
        return True

    """
    For node in tree, it has one indegree, two outdegree (2 children and 1 parent), 
    except root node which has two children no parent.
    For leaf in tree, it has one indegree (1 parent)
    
    diff = outdegree - indegree . in a tree, anytime , diff should >= 0
    if diff < 0, it means indegree > outdegree, some node has more than 2 children. 
    
    When the next nodes comes, diff -= 1 , because the node provides one indegree (include both node and leaf).
    If it's a not leaf node, then diff += 2, because it provides two outdegrees.
    
    For the last , the diff should be zero if it's a valid binary tree.
    """
    def isValidSerialization(self, preorder):
        if not preorder:
            return True
        orders = preorder.split(',')
        diff = 1
        for i in orders:
            diff -= 1
            if diff < 0:
                return False
            if i != '#':
                diff += 2
        return diff == 0

    #update 20210826
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        preorder = preorder.split(',')
        for i, c in enumerate(preorder):
            stack.append(c)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#':
                if stack[-3] == '#':
                    return False
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return stack == ['#']