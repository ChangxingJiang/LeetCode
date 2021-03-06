# LeetCode题解(1081)：不同字符的最小子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/)（中等）

标签：贪心算法、栈、字符串

相关题目：与题目316相同

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 108ms (6.50%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (95.53%) |
| Ans 3 (Python) |            |            |               |

解法一（贪心算法）：

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        if not s:
            return ""
        count = collections.Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            count[s[i]] -= 1
            if count[s[i]] == 0:
                break
        return s[pos] + self.smallestSubsequence(s[pos:].replace(s[pos], ""))
```

解法二（用栈维护最小字典序结果）：

```python
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = collections.Counter(s)
        stack = []
        for ch in s:
            count[ch] -= 1
            if ch not in stack:
                while stack and stack[-1] > ch and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
        return "".join(stack)
```

