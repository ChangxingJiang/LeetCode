# LeetCode题解(1707)：与数组中元素的最大异或值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array/)（困难）

标签：字典树、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N+Q×L)$ | $O(N+Q×L)$ | 5660ms (36.16%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        tree = [{"M": float("inf")} for _ in range(31)]  # 依据最长的2进制长度(<10**9)构造字典树列表
        min_val = min(nums)
        min_bit = min_val.bit_length()

        # 预处理数值，构造字典树
        # O(N)
        for num in set(nums):
            node = tree[num.bit_length()]
            node["M"] = min(node["M"], num)
            for ch in bin(num)[2:]:
                if ch not in node:
                    node[ch] = {"M": num}
                node = node[ch]
                node["M"] = min(node["M"], num)
        # print(tree)

        # 计算生成结果
        # O(Q)
        ans = []
        for x, m in queries:
            # 处理返回-1的情况
            if m < min_val:
                ans.append(-1)
                continue

            # 将X补足长度为x和m的最大值的二进制长度的二进制数
            length = max(x.bit_length(), m.bit_length())
            s = bin(x)[2:].zfill(length)

            # print(x, "->", s, length)

            # 从上到下遍历各个二进制位
            node = None  # 字典树的根节点变量
            for i in range(length):
                bit = length - i  # 计算当前位数（对应的字典树下标）
                ch = s[i]

                # 处理当前还没有开始匹配字典树的情况
                if node is None:
                    if ch == "1":
                        # 处理已经不得不开始匹配字典树的情况，不用考虑字典树是否存在，因为最小值必然存在
                        if bit == min_bit:
                            node = tree[bit]["1"]
                            x -= 2 ** (bit - 1)

                        # 处理还没有不得不开始匹配字典树的情况
                        else:
                            continue

                    else:  # ch == "0"
                        if "1" in tree[bit] and tree[bit]["M"] <= m:  # 如果当前长度有匹配的整数，且大小不超过目标值，则匹配对应的节点
                            node = tree[bit]["1"]
                            x += 2 ** (bit - 1)
                        else:
                            continue

                # 当已经开始匹配字典树的情况
                else:
                    if ch == "1":
                        if "0" in node:
                            node = node["0"]
                        else:
                            x -= 2 ** (bit - 1)
                            node = node["1"]
                    else:  # ch == "0"
                        if "1" in node and node["1"]["M"] <= m:
                            node = node["1"]
                            x += 2 ** (bit - 1)
                        else:
                            node = node["0"]

                # print(i, ":", x, node)

            ans.append(x)

        return ans
```

