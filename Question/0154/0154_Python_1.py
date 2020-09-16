from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


if __name__ == "__main__":
    print(Solution().findMin([1, 3, 5]))  # 1
    print(Solution().findMin([2, 2, 2, 0, 1]))  # 0
