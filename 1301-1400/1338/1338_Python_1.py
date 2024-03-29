import collections
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        target = len(arr) // 2
        now = len(arr)

        ans = 0
        for num in sorted(count.values(), reverse=True):
            now -= num
            ans += 1
            if now <= target:
                break

        return ans


if __name__ == "__main__":
    print(Solution().minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))  # 2
    print(Solution().minSetSize(arr=[7, 7, 7, 7, 7, 7]))  # 1
    print(Solution().minSetSize(arr=[1, 9]))  # 1
    print(Solution().minSetSize(arr=[1000, 1000, 3, 7]))  # 1
    print(Solution().minSetSize(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 5
