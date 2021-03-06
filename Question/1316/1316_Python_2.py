import collections


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        count = collections.defaultdict(collections.deque)
        ans = set()
        for i, ch in enumerate(text):
            for left in count[ch]:
                right = i + (i - left)
                if right > N:
                    break
                if text[left:i] == text[i:right]:
                    ans.add(text[left:right])
            count[ch].appendleft(i)
        return len(ans)


if __name__ == "__main__":
    print(Solution().distinctEchoSubstrings(text="abcabcabc"))  # 3
    print(Solution().distinctEchoSubstrings(text="leetcodeleetcode"))  # 2
