class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
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


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = []
        self.dfs(nestedList)
        self.index = 0
        self.end = len(self.list)

    def dfs(self, nestedlist):
        for nest in nestedlist:
            if nest.isInteger():
                self.list.append(nest.getInteger())
            else:
                self.dfs(nest.getList())

    def next(self):
        """
        :rtype: int
        """
        res = self.list[self.index]
        self.index += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.end
