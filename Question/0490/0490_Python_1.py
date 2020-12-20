import collections
from typing import List


class Solution:
    def __init__(self):
        self.maze = []

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.maze = maze

        start, destination = tuple(start), tuple(destination)

        visited = {start}
        queue = collections.deque([start])
        while queue:
            print(queue)
            now = queue.popleft()
            for next in self.move(now):
                if next == destination:
                    return True
                if next not in visited:
                    queue.append(next)
                    visited.add(next)

        return False

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
            res.append((v1, start[1]))

        # 向下移动
        v2 = start[0]
        for i in range(start[0] + 1, len(self.maze), 1):
            if self.maze[i][start[1]] == 0:
                v2 = i
            else:
                break
        if v2 != start[0]:
            res.append((v2, start[1]))

        # 向左移动
        v3 = start[1]
        for j in range(start[1] - 1, -1, -1):
            if self.maze[start[0]][j] == 0:
                v3 = j
            else:
                break
        if v3 != start[1]:
            res.append((start[0], v3))

        # 向右移动
        v4 = start[1]
        for j in range(start[1] + 1, len(self.maze[0]), 1):
            if self.maze[start[0]][j] == 0:
                v4 = j
            else:
                break
        if v4 != start[1]:
            res.append((start[0], v4))

        # print("MOVE:", start, "->", res, "(", v1, v2, v3, v4, ")")

        return res


if __name__ == "__main__":
    # True
    print(Solution().hasPath(
        maze=[
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]
        ],
        start=[0, 4],
        destination=[4, 4]
    ))

    # False
    print(Solution().hasPath(
        maze=[
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]
        ],
        start=[0, 4],
        destination=[3, 2]
    ))
