from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        pass


if __name__ == "__main__":
    # 0.25000
    print(Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2))

    # 0.30000
    print(Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2))

    # 0.00000
    print(Solution().maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2))
