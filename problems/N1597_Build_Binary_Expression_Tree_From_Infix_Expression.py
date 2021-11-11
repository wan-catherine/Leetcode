class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # TLE
    def expTree(self, s):
        """
        :type s: str
        :rtype: Node
        """
        flag = False
        for c in s:
            if c in "+-*/":
                flag = True
                break
        if not flag:
            return Node(s)

        count = 0
        length = len(s)
        for i in range(length - 1, -1, -1):
            c = s[i]
            if c == ')':
                count += 1
            elif c == '(':
                count -= 1

            if count == 0 and c in '+-':
                left, right = self.expTree(s[:i]), self.expTree(s[i+1:])
                return Node(c, left, right)

        count = 0
        for i in range(length - 1, -1, -1):
            c = s[i]
            if c == ')':
                count += 1
            elif c == '(':
                count -= 1

            if count == 0 and c in '*/':
                left, right = self.expTree(s[:i]), self.expTree(s[i + 1:])
                return Node(c, left, right)
        return self.expTree(s[1:-1])

    """
    First : get the postfix expression , so that we don't need to consider the parentheses and the precedence of operator
        use two stacks : res and operators 
        rules：
            1. if c is a number , then directly append into res
            2, if c is not a number which means c in "()+_*/":
                if c == '(' : directly append into the operators 
                if c == ')' : pop all operators include '(' out and put them into res (not include '(')
                if c in '*/' : pop '*/' operators into res, then append it into operators
                if c in '-+' : pop all operators until meets '(' into res, then append it operators
    Second : create tree from the postfix expression
        use one stack : 
            1. create a Node(c)
            2. if c is a number , append into the res
            3. if c is a operator , pop two items from res and as this new Node's left and right 
                notice here , right pop first , then left pop.
    """
    def expTree(self, s):
        def get_post_order(s):
            res = []
            operators = []
            for c in s:
                if c in '0123456789':
                    res.append(c)
                elif c == '(':
                    operators.append(c)
                else:
                    if c == ')':
                        while operators and operators[-1]!= '(':
                            res.append(operators.pop())
                            if operators and operators[-1] == '(':
                                operators.pop()
                                break
                    elif c in '*/':
                        while operators and operators[-1] in '*/':
                            res.append(operators.pop())
                        operators.append(c)
                    else:
                        while operators and operators[-1] != '(':
                            res.append(operators.pop())
                        operators.append(c)
            while operators:
                res.append(operators.pop())
            return res

        post_order = get_post_order(s)

        def create_tree(s):
            stack = []
            for c in s:
                node = Node(c)
                if c in '+-*/':
                    node.right = stack.pop()
                    node.left = stack.pop()
                stack.append(node)
            return stack[0]

        return create_tree(post_order)



