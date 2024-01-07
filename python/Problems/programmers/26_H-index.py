# 정렬
"""
- 정렬 순서도 중요하다.
- 이 문제의 경우, 지금 idx 보다 이상인 것을 찾기 위해서는 내림차순(reverse)로 정렬해서, 현재 idx 를 가져오는 것이 유리하다. 
"""


def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    for i, citation in enumerate(citations):
        if i >= citation:
            return i
    return 0


citations = [3, 0, 6, 1, 5]
print(solution(citations))
