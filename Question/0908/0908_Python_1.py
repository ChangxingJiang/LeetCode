from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(max(A) - min(A) - 2 * K, 0)


if __name__ == "__main__":
    print(Solution().smallestRangeI(A=[1], K=0))  # 0
    print(Solution().smallestRangeI(A=[0, 10], K=2))  # 6
    print(Solution().smallestRangeI(A=[1, 3, 6], K=3))  # 0
