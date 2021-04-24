import bisect
import collections
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # 统计每个点的连接数量&相互连接数量：O(E)
        count_num = [0] * n
        count_cross = collections.defaultdict(collections.Counter)
        for u, v in edges:
            count_num[u - 1] += 1
            count_num[v - 1] += 1
            count_cross[u - 1][v - 1] += 1
            count_cross[v - 1][u - 1] += 1

        # 排序连接数量：O(NlogN)
        sorted_num = sorted(count_num)

        ans = []

        for query in queries:
            res = 0

            # 统计每个结点可以选择的结点数量
            # 每个结点都考虑除自己以外所有的边，最终得出结果的2倍
            for i in range(n):
                # 如果当前结点的连接的边数已经达到查询要求，则当前结点所有连接的边均符合要求
                if count_num[i] > query:
                    res += (n - 1)

                # 如果当前结点的连接的边数未达到查询要求，则二分查找相邻的符号的点对
                else:
                    # 计算还需要的边数量
                    need = query - count_num[i]

                    # 二分查找符合条件的边（暂不考虑点对本身就是一条/多条边；暂不考虑将自身算在内的情况）
                    # 单次：O(logN)；累计：O(QNlogN)
                    idx = bisect.bisect_right(sorted_num, need)
                    res += (n - idx)

                    # 将自身剔除（如果被算进去的话）
                    if count_num[i] > need:
                        res -= 1

                    # 处理点对本身就是一条/多条边的情况，如果不足要求则剔除
                    # 单次：O(E/N)；累计：O(QE)
                    for j in count_cross[i]:
                        # 按此前方法计算被计入，但实际上不符合查询要求的情况
                        if count_num[i] + count_num[j] > query >= count_num[i] + count_num[j] - count_cross[i][j]:
                            res -= 1

            ans.append(res // 2)

        return ans


if __name__ == "__main__":
    # [6,5]
    print(Solution().countPairs(n=4, edges=[[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], queries=[2, 3]))

    # [10,10,9,8,6]
    print(Solution().countPairs(n=5, edges=[[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]],
                                queries=[1, 2, 3, 4, 5]))
