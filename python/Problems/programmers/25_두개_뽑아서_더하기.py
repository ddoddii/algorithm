from itertools import combinations

"""
배열 중 2개를 뽑아서 더한다 -> 순서가 상관 없으므로 조합(combinations) 이용 
"""


def solution(numbers):
    answer = set()
    for i in map(list, combinations(numbers, 2)):
        answer.add(sum(i))
    return sorted(list(answer))


numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
