# LeetCode题解(0575)：分糖果(Python)

题目：[原题链接](https://leetcode-cn.com/problems/distribute-candies/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 972ms (97.91%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（集合法）：

```python
def distributeCandies(self, candies: List[int]) -> int:
    return min(len(set(candies)), len(candies) // 2)
```