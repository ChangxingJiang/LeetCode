class Solution:
    def minimumBoxes(self, n: int) -> int:
        # ---------- 计算可以堆放的最大层数 ----------
        level = 1
        cell = 0
        while cell + (1 + level) * level // 2 <= n:
            cell += (1 + level) * level // 2
            level += 1
        level -= 1

        # 计算当前占地面积（即最下层的盒子数量）
        area = (1 + level) * level // 2

        # ---------- 计算还需要继续放置的砖块 ----------
        now = 0
        while cell < n:
            area += 1
            cell += now + 1
            now += 1

        return area


if __name__ == "__main__":
    print(Solution().minimumBoxes(1))  # 1
    print(Solution().minimumBoxes(3))  # 3
    print(Solution().minimumBoxes(4))  # 3
    print(Solution().minimumBoxes(5))  # 4
    print(Solution().minimumBoxes(6))  # 5
    print(Solution().minimumBoxes(7))  # 5
    print(Solution().minimumBoxes(10))  # 6

    print(Solution().minimumBoxes(11))  # 7
    print(Solution().minimumBoxes(12))  # 8
    print(Solution().minimumBoxes(13))  # 8
    print(Solution().minimumBoxes(14))  # 9
    print(Solution().minimumBoxes(15))  # 9
