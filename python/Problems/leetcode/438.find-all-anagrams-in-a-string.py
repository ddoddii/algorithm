#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return None
        answer = []
        pMap = {}
        for letter in p:
            pMap[letter] = pMap.get(letter, 0) + 1

        subString = s[0 : len(p)]
        subMap = {}
        for letter in subString:
            subMap[letter] = subMap.get(letter, 0) + 1
        if subMap == pMap:
            answer.append(0)
        for i in range(1, len(s) - len(p) + 1):
            subMap[s[i - 1]] = subMap.get(s[i - 1]) - 1
            if subMap[s[i - 1]] == 0:
                del subMap[s[i - 1]]
            subMap[s[i + len(p) - 1]] = subMap.get(s[i + len(p) - 1], 0) + 1
            if pMap == subMap:
                answer.append(i)
        return answer

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        char_freqs, answer, len_p, len_s = defaultdict(int), [], len(p), len(s)
        for char in p:
            char_freqs[char] += 1

        # first window (0 ~ len(p)-1)
        for i in range(len_p - 1):
            if s[i] in char_freqs:
                char_freqs[s[i]] -= 1

        # slide window
        for i in range(len_p - 1, len_s):
            # remove front
            j = i - len_p
            if j >= 0 and s[j] in char_freqs:
                char_freqs[s[j]] += 1
            # add back
            if s[i] in char_freqs:
                char_freqs[s[i]] -= 1

            # check if all char freq is 0
            if all(v == 0 for v in char_freqs.values()):
                answer.append(j + 1)
        return answer


sol = Solution()
s = "cbaebabacd"
p = "abc"

print(sol.findAnagrams2(s, p))

# @lc code=end
