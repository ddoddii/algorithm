#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        dic = defaultdict(list)
        for root in dictionary:
            dic[root[0]].append(root)
        new_sentence = []
        for word in words:
            candidates = dic[word[0]]
            if not candidates:
                new_sentence.append(word)
                continue
            candidates.sort(key=len)
            found = False
            for candidate in candidates:
                n = len(candidate)
                if word[:n] == candidate:
                    new_sentence.append(candidate)
                    found = True
                    break
            if not found:
                new_sentence.append(word)

        return " ".join(new_sentence)

    def replaceWords2(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        n = len(words)
        for i in range(n):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
        return " ".join(words)


dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(Solution().replaceWords2(dictionary, sentence))
# @lc code=end
