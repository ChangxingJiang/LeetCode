# LeetCode题解(1578)：使字符串相邻字母不相同的最小删除成本(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/)（中等）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 392ms (28%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] == s[i]:
                j += 1
            else:
                if j - i > 1:
                    ans += sum(cost[i:j]) - max(cost[i:j])
                i = j
        else:
            if j - i > 1:
                ans += sum(cost[i:j]) - max(cost[i:j])
        return ans
```