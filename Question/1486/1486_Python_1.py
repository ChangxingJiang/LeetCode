class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans


if __name__ == "__main__":
    print(Solution().xorOperation(n=5, start=0))  # 8
    print(Solution().xorOperation(n=4, start=3))  # 8
    print(Solution().xorOperation(n=1, start=7))  # 7
    print(Solution().xorOperation(n=10, start=5))  # 2
