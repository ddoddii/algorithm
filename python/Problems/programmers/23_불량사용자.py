# 완전 탐색

import re
from itertools import permutations

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

"""
- 비트마스킹 풀이 : https://ddoddii.github.io/post/cs/algorithm/bitmasking/ 보기
"""


def solution(user_id, banned_id):
    answer = set()
    banPatterns = [x.replace("*", ".") for x in banned_id]
    search(0, 0, user_id, answer, banPatterns)
    print(answer)
    return len(answer)


def search(idx, visit, userId, answer, banPatterns):
    if idx == len(banPatterns):
        answer.add(visit)
        print(f"answer: {answer}")
        return

    for i in range(len(userId)):
        a = visit & (1 << i)
        if (visit & (1 << i)) > 0 or not re.fullmatch(banPatterns[idx], userId[i]):
            continue
        print(visit)
        b = visit | (1 << i)
        search(idx + 1, visit | (1 << i), userId, answer, banPatterns)


"""
- 순열 이용
"""


def solution2(user_id, banned_id):
    answer = set()
    banned = " ".join(banned_id).replace("*", ".")

    for i in permutations(user_id, len(banned_id)):
        if re.fullmatch(banned, " ".join(i)):
            answer.add("".join(sorted(i)))
            print(answer)
    return len(answer)


print(solution2(user_id, banned_id))
