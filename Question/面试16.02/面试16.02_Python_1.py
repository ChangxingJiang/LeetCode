from typing import List
import collections

class WordsFrequency:

    def __init__(self, book: List[str]):
        self.count = collections.Counter(book)

    def get(self, word: str) -> int:
        return self.count[word]


if __name__ == "__main__":
    wf = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
    print(wf.get("you"))  # 0
    print(wf.get("have"))  # 2
    print(wf.get("an"))  # 1
    print(wf.get("apple"))  # 1
    print(wf.get("pen"))  # 1
