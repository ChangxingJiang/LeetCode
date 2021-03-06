# LeetCode题解(1281)：各位数字的积与和之差(Python)

题目：[原题链接](https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 32ms (96.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def subtractProductAndSum(self, n: int) -> int:
    product = 1
    total = 0
    while n:
        digit = n % 10
        n = n // 10
        product *= digit
        total += digit
    return product - total
```