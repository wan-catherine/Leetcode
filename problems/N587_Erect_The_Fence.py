from typing import List

"""
Convex Hull problem. 
Here I use Monotone chain convex hull. 
"""
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orietation(p, q, r):
            return (q[1] - p[1]) * (r[0] - p[0]) > (r[1] - p[1]) * (q[0] - p[0])

        trees.sort()
        stack = []
        for i, j in trees:
            while len(stack) >= 2 and orietation(stack[-2], stack[-1], [i, j]):
                stack.pop()
            stack.append((i,j))
        stack.pop()
        for i, j in trees[::-1]:
            while len(stack) >= 2 and orietation(stack[-2], stack[-1], [i, j]):
                stack.pop()
            stack.append((i, j))
        return list(set(stack))
