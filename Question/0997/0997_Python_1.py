from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        maybe = [0 for _ in range(N)]
        for t in trust:
            maybe[t[0] - 1] -= 1
            maybe[t[1] - 1] += 1
        for i in range(N):
            if maybe[i] == N-1:
                return i+1
        else:
            return -1


if __name__ == "__main__":
    print(Solution().findJudge(N=2, trust=[[1, 2]]))  # 2
    print(Solution().findJudge(N=3, trust=[[1, 3], [2, 3]]))  # 3
    print(Solution().findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))  # -1
    print(Solution().findJudge(N=3, trust=[[1, 2], [2, 3]]))  # -1
    print(Solution().findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))  # 3
