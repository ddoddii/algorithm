# 이분탐색
"""
- 1명씩 건넌다고 생각하지 말고, n 명이 건너려면 징검다리가 어느 조건이어야 하는지? 생각
- 
"""


def solution(stones, k):
    answer = 0
    start, end = 0, max(stones)
    while start <= end:
        mid = (start + end) // 2
        # n 명이 건널 수 있으면 범위를 mid 보다 크게 늘린다.
        if available(mid, stones, k):
            start = mid + 1
            answer = max(answer, mid)
        # n 명이 건널 수 없으면 범위를 mid 보다 작게 줄인다.
        else:
            end = mid - 1
    return answer


def available(n, stones, k):
    skip = 0
    for stone in stones:
        if stone < n:
            skip += 1
            if skip >= k:
                return False
        else:
            skip = 0
    return True


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))
