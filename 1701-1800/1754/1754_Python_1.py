class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        size1, size2 = len(word1), len(word2)

        ans = []

        i1, i2 = 0, 0
        while i1 < size1 and i2 < size2:
            if word1[i1:] > word2[i2:]:
                ans.append(word1[i1])
                i1 += 1
            else:
                ans.append(word2[i2])
                i2 += 1

        if i1 < size1:
            ans.append(word1[i1:])
        if i2 < size2:
            ans.append(word2[i2:])

        return "".join(ans)


if __name__ == "__main__":
    # "cbcabaaaaa"
    print(Solution().largestMerge(word1="cabaa", word2="bcaaa"))

    # "abdcabcabcaba"
    print(Solution().largestMerge(word1="abcabc", word2="abdcaba"))

    # 测试用例 90/101
    # "uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu"
    print(Solution().largestMerge(word1="uuurruuuruuuuuuuuruuuuu",
                                  word2="urrrurrrrrrrruurrrurrrurrrrruu"))

    # 测试用例 97/101
    print(Solution().largestMerge(
        word1="uuuuuuuuujuujuuuuuuuujuuuuuuuujujuuuuuuujuuuuuuuuuuuujuuujujjuujuuuuuuuuuuuuuuuujuuuuuuuuuuuuuuuuujujuuuuuuuuuuuuuuuuuujuuuujuuuujuuuuujuuuujuuuujuuuuuuuuuujujuuuuujujuuuujjujuujjuuuuuuujujjuuujjjjjuuujuujjuujujujuujuujujuujuuuujuuuuuuuuuuuuuuuuuuuujjuuuuuujuuuuuuuuuuuuuuuuuujujuuuuuuujujjuuuuuuuuujuuuuuuuuujuuujujjjjujjuuuuujuuuuuuujuuuuuuuuuuuujjuuuuuuuuuuujuuuujuujjuuuujuuuujuuuuuuuuuuuujjuuuuuuuujuujuuuuujuuuuuuuuuujjuuuuuuuujuuujjuuuuuuujuujjjuuuuujuuujujuuuuuuuuuuuuuuuujuuuuujuuuuuujuujujuuuuuuujuuuuuujuujuuuujjuuuuuuujuuuuuujuuuuujjujuuuuuuuuuuujuujjuuujuuuuuuuuuuuuujujuuuujujuuujuuuuuuujuuuuuuujujuuujuuuuuuuuuuujuuuujuujjjuuujuuuuujuuuuuujujujujujuuuuuuuuuujuuujuujuuuuujuuuujjuuuuuujujjuuujujuuuujuuuuuuujuuuuuuuuuujuuujuuuuuuujuuujujuuuuuuuuuuuuuuuuujuuujjuuuuuuuuujuuujuuuuuuuuuujjjuuuuuuuuuuujjuujuujuuuuuujuuuuuujuuuuuuuuuuujujuuujuuujujjuuuuuuujuuuuuuuuuujuuujuuuuujuuuuuuuuuujuuujjjujuuujuujujuuuuuuuujuuuujuuuuujuujujuuujuujuuuuuuuuujuujuuuuuuuujuuuuuuuuuuuuuuujuuujjuuuuuuuuuuuuujuuuuuuuuuujuuuuujuuuuuuuuuuuuuujuujuujjuujujuujuuuuuujuuuuuujuuuuuuuuuuuuuuuujuujuuuuuuuuujuujuuuuujuuuujjuujuuujuuuuuuuuuuujuuuujjuuuuuujuuujuuujjujuuuuuuuuuuuuuuujuuuuujuuuuujuuujjjuuujuuuuuuuuuujuujjujujuujuujuuuujuuuuuuuuuujjuuuuuuujuuuujuuuujuuuuuuuuuujuujujujuuuuuuujuuuuuuuuuuuujuuujjuuuuujuuuuuuuuuuuuuuuuuuuujuujuuuuuuuuuuuujuuuujuuuujjjuujuuuuuuujjuuujuuuuuuuuuuuuuuuujujuuuuujujujuuuuuuuuujuuuuuuuuuuuuuuuuuuuuujuuuuuuuuuuuuujujjujuuuuuuuuuujuuujujuuuuuuuuuujjuujuujuuujuuuuujujujujuuuuuuuuuuuuuuuuuuuuuuuujuuuujuuuujjuuuuuuuuuuuuuuuuuuuuuujuuuuuuuuuuuuuuuuuuuuuuuuuuujuuuuujuuuuujuuuuuuuuuuuuuuuujuuuuuujujujuujujjuujuujujuujuuuuuuuuuuuujuuujjjuuuuuuuujjuuuuuuujuuuuuuuuuuuuuuujuuuuuuuuuuuujuuuuuuuuuuuuuuujjuuuuuuuuujjjuuuuuuujuuuuuuujujjuuuuujuujuuujuuuuuuuuuuuujujjjuuuujuuuuujjuuuuuuuujjujuuuuuuuuuuuujjjuuujuujuuuuuuuuuuuuuuujuuuuuuuujujujuujuuuuuujuuujuuuuuuuuuuujuuuuujujuuujuuuuuuuuujuujuuuuuuuuuujuuuuuuuuuujuujuuuuuujuuuuuuuuuuuuuuuujuuuuuujuuuujuuuuuujuuuuujuuuuuuuujujuuujuujjuuuujuuuuuujuuuuujuujjujujuujuuuuuujujuuuuuuujuuujuuujuuuuuuuuuuujuuuuuujujjujuuuuujuuuuujujuujjuuuuuuuujjjuujuuuuuuuuujuuuuuuuuuuuuuuujujuuuujuuuuujuuuuuuuujuuuuuuuuuuuuuuuuuujuuuuuuuuujjujuuuuujuuuuuuuujujuuujuuujjujuuuuuuuuuuuuuuujujuuuuuujuuuuuuuuuuuuujjuuuuuuuuujuuuujuuuuuuuujuuuuujuuuuuuuuuujujuuuuuuuuuuuuuujuuuuujjuuuuuuujuuujuujuuuuuujuuujuuuuuujujuujujuuuuuujujuuuuujuuuuujujujuujjjjuuuuuuuujujuujuuujuuuuuu",
        word2="uuujuujujjjjjjjuujjjjuujjjjjjjjjjjjuujjjjujjjuujujujjjjjjjjjjjjjjjjujujjjjujjjjjjjjjujjjjjjjjjjjjuujjjjjuujujjjjjjjjujjujjjujjjjjjjjjjjjjjjjujjjjjjjjujjjjjjjjjjjjjjjujuuujujujjjujujjuujjjjjjjjjujjjjjjjujjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjjjujjjjjujjujujjjjjjjuujjjjjjjjjjjjujjjjjjjjjjjjjjjjjujujjjujjjjjjjjujjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjuuujjjjjjjjujujjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjujjjjjjjjjjjjjujjujjjjjjujujjjjjjjjjujjjjjjjjjjjjjjjjjjjjjujjjjjujjjujjjjjjjjjjjjjjjjjjjjujjjjjjjjujjjjjjjjjjjjjjjjjjuujjjjjjjujjjuujjjjjjjjjjjjjjjjjjjujjjujjjjjujjjjjuujjjjjjjjuujjujjjjjjjjjjjjjjjujjujjjjjjjjujujjujjjuujjjjjjjjjjjjjjjujjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjujjjjujjjjjjjjjjjjjuujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjjjuujjjjjujjjjjjjjjujjjjjjujjjjjjjjjjjjjjjjjuujjjjjjjjjjjjjjjjjjjjjujjjjjujujjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjujujjuujjjjjjjjjjjjjjjjjjjujjjjjujujjjjjjujjuujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjuuujjjjjjjuujjjjjjjjjjjjjjujjjjjjjjjujjjjujjjujjjjjjjjjjjjjjjjjujjujjjjjjjjjjjjjjjjujuuujjjujjjjjjjjjjjjujjjujjjjjujjjjjjjjujjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjujjjujujjujjjujujjjjujjjjjjjjjjjuujuujjjjujjjjjjjjjujjjjjjjjujjjjjjjjujjjujjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjuuujjjjjjjjujujujjujjjujjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjujujjjjuujjjujujjjjjujjjjjjjjjjjjjjjujjjjujjjujjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjjjjujjuujujjujjjjjjjjjjjjjjujjjjjjujjjjjjjjjjujjjjuuujjjjjjjjujjuujjjjjjjujjjjjjjujjjjujujjjjjjjjjjjjjjjjjjjjjjjjjjuujjjjjjjjjjjjjujjjjjjjjuujjjujjjjujjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjujjujujjjjjjjjjjjjujjjjjjjjujjjjujjujuujjjjjujjjjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjjjjujjjujujjjjjjjjjjjjjjjjujjjjjjujjuujjjjjujjjjjjjujjjjuujjjujjjjjjjjjjjjjjjjujjjjjjjjjjjjujjjjjuuuujjjujjjjjjjjjjjjjjuujuujjjjjjjjjjujujjjjujjujjjjjjujjujjujjjjjjjujujujjujjjjjjjujjjjujjuuujjjjjjjjjjjjjjjjjjujjjjjjjjjjjjjjjjujjjujjjjjjjjjujjjjjjjjujjjjjjjjjjjjjjjujjjjjjujjjjjjjjujjjjjjjujjjjjujjjjjjjujjujjjjjjjjjjjjjujjju"))