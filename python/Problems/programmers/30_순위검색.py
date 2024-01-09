# 이진 탐색
"""
- 전부 다 탐색해야 하는데 , 그러면 시간복잡도 O(n^2) 이어서 효율성 테스트에서 실패했다.
- '-' 면 모두 매칭하는게 키 포인트 !! -> 미리 가능한 조합을 딕셔너리로 구현해놓으면, 대조하는 것은 O(1) 로도 가능하다.
- 효율성을 통과하기 위해서 미리 key (사람의 정보) , value(점수) 대응하는 딕셔너리를 만들었다.
- 쿼리의 정보를 people 의 key 에서 찾아서, 점수 이상인 사람 이진탐색 (bisect_left) 로 찾았다.
"""
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    people = defaultdict(list)

    for i in info:
        person = i.split()
        score = int(person.pop())
        people["".join(person)].append(score)

        for j in range(4):
            case = list(combinations(person, j))
            for c in case:
                people["".join(c)].append(score)

    for i in people:
        people[i].sort()
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = "".join(key)
        key = key.replace("and", "").replace(" ", "").replace("-", "")
        answer.append(len(people[key]) - bisect_left(people[key], score))

    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]

query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]

print(solution(info, query))
