from typing import List


class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().getTriggerTime(increase=[[2, 8, 4], [2, 5, 0], [10, 9, 8]],
                                    requirements=[[2, 11, 3], [15, 10, 7], [9, 17, 12], [8, 1, 14]]))  # [2,-1,3,-1]
    print(Solution().getTriggerTime(increase=[[0, 4, 5], [4, 8, 8], [8, 6, 1], [10, 10, 0]],
                                    requirements=[[12, 11, 16], [20, 2, 6], [9, 2, 6], [10, 18, 3],
                                                  [8, 14, 9]]))  # [-1,4,3,3,3]
    print(Solution().getTriggerTime(increase=[[1, 1, 1]], requirements=[[0, 0, 0]]))  # [0]