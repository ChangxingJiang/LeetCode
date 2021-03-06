# LeetCode题解(1494)：并行课程II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/parallel-courses-ii/)（困难）

标签：图、动态规划、拓扑排序

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时        |
| -------------- | ------------ | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2×2^N)$ | $O(2^N)$   | 3480ms (31.82%) |
| Ans 2 (Python) | $O(N^2×2^N)$ | $O(2^N)$   | 472ms (59.09%)  |
| Ans 3 (Python) |              |            |                 |

解法一：

```python
class Solution:
    def __init__(self):
        self.dp = []  # 状态矩阵：dp[state]表示状态为完成状态state的课至少需要几个学期

    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 初始化状态矩阵
        self.dp = [-1] * (1 << (n + 1))
        self.dp[0] = 0

        # 计算每门课程的前置课程的状态
        pre_state = [0] * (n + 1)
        for c1, c2 in dependencies:
            pre_state[c2] |= (1 << c1)

        for state in range(1 << (n + 1)):
            # 如果当前课程状态不存在，则跳过当前课程状态
            if self.dp[state] == -1:
                continue

            # 寻找下一门可以学习的课程
            course = []
            for i in range(1, n + 1):
                # 如果这门课程已经被学过了
                if (state >> i) & 1 == 1:
                    continue

                # 如果这门课程的前置条件还没有被完成
                if (state & pre_state[i]) != pre_state[i]:
                    continue

                course.append(i)

            self.dfs(x=0, m=len(course), k=min(len(course), k), step=self.dp[state] + 1, state=state, course=course)
        return self.dp[-2]

    def dfs(self, x, m, k, step, state, course):
        """深度优先搜索

        :param x: 当前已经遍历到的下一门可以学习的课程坐标
        :param m: 下一个学期可以学习的课程数量
        :param k: 下一个学期可以学习的课程数量上限
        :param step: 当前的学期数量
        :param state: 当前课程学习情况
        :param course: 下一门可以学习的课程
        """
        # 如果当前学期已经安排完成
        if x >= m or k == 0:
            if self.dp[state] == -1 or self.dp[state] > step:
                self.dp[state] = step
        else:
            self.dfs(x + 1, m, k - 1, step, state | (1 << course[x]), course)  # 深度优先搜索:选择当前课程
            self.dfs(x + 1, m, k, step, state, course)  # 深度优先搜索:不选择当前课程
```

解法二（增加剪枝条件）：

```python
class Solution:
    def __init__(self):
        self.dp = []  # 状态矩阵：dp[state]表示状态为完成状态state的课至少需要几个学期

    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 初始化状态矩阵
        self.dp = [-1] * (1 << (n + 1))
        self.dp[0] = 0

        # 计算每门课程的前置课程的状态
        pre_state = [0] * (n + 1)
        for c1, c2 in dependencies:
            pre_state[c2] |= (1 << c1)

        for state in range(1 << (n + 1)):
            # 如果当前课程状态不存在，则跳过当前课程状态
            if self.dp[state] == -1:
                continue

            # 寻找下一门可以学习的课程
            course = []
            for i in range(1, n + 1):
                # 如果这门课程已经被学过了
                if (state >> i) & 1 == 1:
                    continue

                # 如果这门课程的前置条件还没有被完成
                if (state & pre_state[i]) != pre_state[i]:
                    continue

                course.append(i)

            self.dfs(x=0, m=len(course), k=min(len(course), k), step=self.dp[state] + 1, state=state, course=course)
        return self.dp[-2]

    def dfs(self, x, m, k, step, state, course):
        """深度优先搜索

        :param x: 当前已经遍历到的下一门可以学习的课程坐标
        :param m: 下一个学期可以学习的课程数量
        :param k: 下一个学期可以学习的课程数量上限
        :param step: 当前的学期数量
        :param state: 当前课程学习情况
        :param course: 下一门可以学习的课程
        """
        # 剪枝条件:本学期已无法达到理论最高效的情况
        if m - x < k:
            return

        # 如果当前学期已经安排完成
        if x >= m or k == 0:
            if self.dp[state] == -1 or self.dp[state] > step:
                self.dp[state] = step
        else:
            self.dfs(x + 1, m, k - 1, step, state | (1 << course[x]), course)  # 深度优先搜索:选择当前课程
            self.dfs(x + 1, m, k, step, state, course)  # 深度优先搜索:不选择当前课程
```

