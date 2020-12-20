from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
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
    def __init__(self):
        self.ans = [[]]

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.dfs(nestedList, 0)

        ans = 0
        for i in range(len(self.ans)):
            height = len(self.ans) - i
            ans += height * sum(self.ans[i])
        return ans

    def dfs(self, lst, depth):
        if len(self.ans) < depth + 1:
            self.ans.append([])
        for elem in lst:
            if elem.isInteger():
                self.ans[depth].append(elem.getInteger())
            else:
                self.dfs(elem.getList(), depth + 1)


if __name__ == "__main__":
    pass
