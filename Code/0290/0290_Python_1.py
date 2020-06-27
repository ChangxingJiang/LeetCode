class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(" ")
        if len(pattern) != len(words):
            return False
        hashmap = {}
        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                if words[i] not in hashmap.values():
                    hashmap[pattern[i]] = words[i]
                else:
                    return False
            else:
                if hashmap[pattern[i]] != words[i]:
                    return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().wordPattern("abba", "dog cat cat dog"))  # True
    print(Solution().wordPattern("abba", "dog cat cat fish"))  # False
    print(Solution().wordPattern("aaaa", "dog cat cat dog"))  # False
    print(Solution().wordPattern("abba", "dog dog dog dog"))  # False
