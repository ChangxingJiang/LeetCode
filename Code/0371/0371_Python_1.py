class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])


if __name__ == "__main__":
    print(Solution().getSum(1, 2))  # 3
    print(Solution().getSum(-2, 3))  # 1
