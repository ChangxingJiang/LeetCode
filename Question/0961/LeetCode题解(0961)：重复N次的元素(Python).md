# LeetCode题解(0961)：重复N次的元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

![LeetCode题解(0961)：截图1](LeetCode题解(0961)：截图1.png)

```python
def repeatedNTimes(self, A: List[int]) -> int:
    hashmap = set()
    for a in A:
        if a not in hashmap:
            hashmap.add(a)
        else:
            return a
```