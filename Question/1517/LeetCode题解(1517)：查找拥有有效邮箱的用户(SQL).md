# LeetCode题解(1517)：查找拥有有效邮箱的用户(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/find-users-with-valid-e-mails/)（简单）

标签：SQL

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) |            |            | 478ms (67.12%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```mysql
SELECT *
FROM Users
WHERE mail REGEXP '^[a-zA-Z]+[\\w/.\\-]*(@leetcode.com)$';
```