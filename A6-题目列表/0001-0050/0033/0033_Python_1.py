from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
    print(Solution().search(nums=[1], target=0))  # -1
