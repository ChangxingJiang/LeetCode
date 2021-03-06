from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B = sorted(A)
        return B == A or B == A[::-1]


if __name__ == "__main__":
    print(Solution().isMonotonic([1, 2, 2, 3]))  # True
    print(Solution().isMonotonic([6, 5, 4, 4]))  # True
    print(Solution().isMonotonic([1, 3, 2]))  # False
    print(Solution().isMonotonic([1, 2, 4, 5]))  # True
    print(Solution().isMonotonic([1, 1, 1]))  # True
