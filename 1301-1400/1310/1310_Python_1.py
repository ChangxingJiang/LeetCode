from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        now = 0
        for num in arr:
            now ^= num
            xor.append(now)

        ans = []
        for l, r in queries:
            ans.append(xor[r + 1] ^ xor[l])
        return ans


if __name__ == "__main__":
    # [2,7,14,8]
    print(Solution().xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]))

    # [8,0,4,4]
    print(Solution().xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]))
