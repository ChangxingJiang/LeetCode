import collections
from typing import List


class Solution:
    def __init__(self):
        self.maze = []

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        self.maze = maze

        start, destination = tuple(start), tuple(destination)

        visited = {start: 0}
        queue = collections.deque([(start, 0)])

        ans = float("inf")

        while queue:
            for _ in range(len(queue)):
                now, d1 = queue.popleft()
                for next, d2 in self.move(now):
                    if next == destination:
                        ans = min(ans, d1 + d2)
                    if next not in visited or d1 + d2 < visited[next]:
                        queue.append((next, d1 + d2))
                        visited[next] = d1 + d2

        return ans if ans != float("inf") else -1

    def move(self, start):
        res = []

        # 向上移动
        v1 = start[0]
        for i in range(start[0] - 1, -1, -1):
            if self.maze[i][start[1]] == 0:
                v1 = i
            else:
                break
        if v1 != start[0]:
            res.append(((v1, start[1]), start[0] - v1))

        # 向下移动
        v2 = start[0]
        for i in range(start[0] + 1, len(self.maze), 1):
            if self.maze[i][start[1]] == 0:
                v2 = i
            else:
                break
        if v2 != start[0]:
            res.append(((v2, start[1]), v2 - start[0]))

        # 向左移动
        v3 = start[1]
        for j in range(start[1] - 1, -1, -1):
            if self.maze[start[0]][j] == 0:
                v3 = j
            else:
                break
        if v3 != start[1]:
            res.append(((start[0], v3), start[1] - v3))

        # 向右移动
        v4 = start[1]
        for j in range(start[1] + 1, len(self.maze[0]), 1):
            if self.maze[start[0]][j] == 0:
                v4 = j
            else:
                break
        if v4 != start[1]:
            res.append(((start[0], v4), v4 - start[1]))

        # print("MOVE:", start, "->", res, "(", v1, v2, v3, v4, ")")

        return res


if __name__ == "__main__":
    # 12
    print(Solution().shortestDistance(maze=[
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ], start=[0, 4], destination=[4, 4]))

    # -1
    print(Solution().shortestDistance(maze=[
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ], start=[0, 4], destination=[3, 2]))
