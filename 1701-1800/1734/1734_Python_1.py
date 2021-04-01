from typing import List


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        # 计算每一二进制位与第一个数相同的数量和与第一个数不相同的数量
        size = n.bit_length()
        lst_same = [[1, 0] for _ in range(size)]  # 每一个元素第一项为与第一个数相同的数量，第二项为与第一个数不同的数量
        now = 0  # 当前状态
        for v in encoded:
            now ^= v
            for i in range(size):
                if (1 << i) & now:
                    lst_same[i][1] += 1
                else:
                    lst_same[i][0] += 1

        # 计算第一个数
        # 因为n为奇数，所以说明每一位两种情况的数量必定是有差异的
        first_number = 0
        for i in range(size):
            bit = 1 << (i + 1)

            # 计算当前位为1的总数
            expect_num = (n - n % bit) // 2 + max(0, n % bit - (bit // 2 - 1))

            if lst_same[i][0] == expect_num:
                first_number ^= (1 << i)

        # 计算最终结果
        ans = [first_number]
        for v in encoded:
            ans.append(ans[-1] ^ v)
        return ans


if __name__ == "__main__":
    print(Solution().decode([3, 1]))  # [1,2,3]
    print(Solution().decode([6, 5, 4, 6]))  # [2,4,1,5,3]
