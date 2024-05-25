#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#

# @lc code=start
from typing import List


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        n: int = len(words)
        letters_count: list[int] = [0 for _ in range(26)]
        for letter in letters:
            idx = ord(letter) - ord("a")
            letters_count[idx] += 1
        words_score: dict[str, int] = {}
        for word in words:
            s = 0
            for c in word:
                s += score[ord(c) - ord("a")]
            words_score[word] = s

        res = 0

        def recursion(curr_idx, curr_score):
            nonlocal res

            if curr_idx == n:
                res = max(res, curr_score)
                return

            can_add_word = True
            curr_word = words[curr_idx]
            word_count: list[int] = [0 for _ in range(26)]
            for c in curr_word:
                idx = ord(c) - ord("a")
                word_count[idx] += 1
                if word_count[idx] > letters_count[idx]:
                    can_add_word = False
                    break

            # 단어 추가 가능
            if can_add_word:
                # 쓴 단어만큼 빼기
                for idx in range(26):
                    letters_count[idx] -= word_count[idx]
                # 이 상태에서 재귀
                recursion(curr_idx + 1, curr_score + words_score[curr_word])
                # 다시 복구(backtrack)
                for idx in range(26):
                    letters_count[idx] += word_count[idx]
            # 현재 단어 추가 없이 재귀
            recursion(curr_idx + 1, curr_score)

        recursion(0, 0)

        return res


words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(Solution().maxScoreWords(words, letters, score))
# @lc code=end
