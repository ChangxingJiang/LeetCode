from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().smallestDivisor(nums=[1, 2, 5, 9], threshold=6))  # 5
    print(Solution().smallestDivisor(nums=[2, 3, 5, 7, 11], threshold=11))  # 3
    print(Solution().smallestDivisor(nums=[19], threshold=5))  # 4
