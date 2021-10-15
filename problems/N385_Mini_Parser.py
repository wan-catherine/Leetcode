class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        num = ''
        for x in s:
            if x == '[':
                stack.append(NestedInteger())
            elif x == ']':
                temp = stack.pop()
                if num:
                    temp.add(NestedInteger(int(num)))
                    num = ""
                if not stack:
                    return temp
                stack[-1].add(temp)
            elif x == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
            else:
                num += x
        return NestedInteger(int(num))

