from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for start in startTime:
            if start <= queryTime:
                ans += 1
        for end in endTime:
            if end < queryTime:
                ans -= 1
        return ans


if __name__ == "__main__":
    print(Solution().busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4))  # 1
    print(Solution().busyStudent(startTime=[4], endTime=[4], queryTime=4))  # 1
    print(Solution().busyStudent(startTime=[4], endTime=[4], queryTime=5))  # 0
    print(Solution().busyStudent(startTime=[1, 1, 1, 1], endTime=[1, 3, 2, 4], queryTime=7))  # 0
    print(Solution().busyStudent(startTime=[9, 8, 7, 6, 5, 4, 3, 2, 1], endTime=[10, 10, 10, 10, 10, 10, 10, 10, 10],
                                 queryTime=5))  # 5
