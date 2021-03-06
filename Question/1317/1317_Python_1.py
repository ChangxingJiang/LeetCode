from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            if "0" not in str(i) and "0" not in str(n - i):
                return [i, n - i]


if __name__ == "__main__":
    print(Solution().getNoZeroIntegers(2))  # [1,1]
    print(Solution().getNoZeroIntegers(11))  # [2,9]
    print(Solution().getNoZeroIntegers(10000))  # [1,9999]
    print(Solution().getNoZeroIntegers(69))  # [1,68]
    print(Solution().getNoZeroIntegers(1010))  # [11,999]
