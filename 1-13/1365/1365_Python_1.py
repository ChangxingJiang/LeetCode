from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))  # [4,0,1,1,3]
    print(Solution().smallerNumbersThanCurrent(nums=[6, 5, 4, 8]))  # [2,1,0,3]
    print(Solution().smallerNumbersThanCurrent(nums=[7, 7, 7, 7]))  # [0,0,0,0]
