# 17. Letter Combinations of a Phone Number
"""
- backtracking
"""
from typing import List


def letterCombinations(digits: str) -> List[str]:
    numberToChar = mappingLetters()
    if not digits:
        return []
    combi = []
    answer = []
    for str in digits:
        combi.append(numberToChar[str])
    curr = ""
    recursion(combi, curr, answer, 0)
    return answer


def mappingLetters():
    numberToChar = dict()
    numberToChar["2"] = ["a", "b", "c"]
    numberToChar["3"] = ["d", "e", "f"]
    numberToChar["4"] = ["g", "h", "i"]
    numberToChar["5"] = ["j", "k", "l"]
    numberToChar["6"] = ["m", "n", "o"]
    numberToChar["7"] = ["p", "q", "r", "s"]
    numberToChar["8"] = ["t", "u", "v"]
    numberToChar["9"] = ["w", "x", "y", "z"]
    return numberToChar


def recursion(combi, curr, answer, idx):
    if len(curr) == len(combi):
        answer.append(curr)
        return
    for letter in combi[idx]:
        recursion(combi, curr + letter, answer, idx + 1)


def letterCombinations2(digits: str) -> List[str]:
    if not digits:
        return []
    res = []
    digitsToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, curr):
        if len(curr) == len(digits):
            res.append(curr)
            return
        for c in digitsToChar[digits[i]]:
            backtrack(i + 1, curr + c)

    backtrack(0, "")
    return res
