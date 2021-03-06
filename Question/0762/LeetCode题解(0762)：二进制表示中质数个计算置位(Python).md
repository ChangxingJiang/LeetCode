# LeetCode题解(0762)：二进制表示中质数个计算置位(Python)

题目：[原题链接](https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 200ms (99.05%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

![LeetCode题解(0762)：截图1](LeetCode题解(0762)：截图1.png)

> **【思路】**
>
> 因为L≤R≤10^6≤2^20，所以我们只需要枚举20以内的质数即可。

```python
def countPrimeSetBits(self, L: int, R: int) -> int:
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    ans = 0
    for i in range(L, R + 1):
        if bin(i).count("1") in primes:
            ans += 1
    return ans
```