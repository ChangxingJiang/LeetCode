from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        sum_ = 0
        max_ = 0
        min_ = float("inf")
        for s in salary:
            sum_ += s
            max_ = max(max_, s)
            min_ = min(min_, s)
        return (sum_ - max_ - min_) / (len(salary) - 2)


if __name__ == "__main__":
    print(Solution().average(salary=[4000, 3000, 1000, 2000]))  # 2500.00000
    print(Solution().average(salary=[1000, 2000, 3000]))  # 2000.00000
    print(Solution().average(salary=[6000, 5000, 4000, 3000, 2000, 1000]))  # 3500.00000
    print(Solution().average(salary=[8000, 9000, 2000, 3000, 6000, 1000]))  # 4750.00000
