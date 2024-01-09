# 이진탐색
"""
- 가장 짧은 거리 정하고, 돌을 제거했을 때 짧은 거리보다 크게끔 제거한다.
- 제거해야 할 바위가 목표보다 많으면 거리를 줄이고, 목표보다 작으면 거리를 늘린다.
"""
from itertools import combinations


def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    # 도착지점 추가
    rocks.append(distance)
    rocks.sort()

    while start <= end:
        mid = int((start + end) // 2)
        removed = 0
        temp = 0

        for rock in rocks:
            # 설정한 제일 짧은 거리(mid) 보다 작으면 돌 제거
            if rock - temp < mid:
                removed += 1
            # 설정한 제일 짧은 거리(mid) 보다 크므로 제거하지 않음. 새롭게 거리를 잴 기준(temp) 에 돌 위치 저장
            else:
                temp = rock
            if removed > n:
                break

        # 목표보다 더 많은 바위 제거 시 거리 줄인다.
        if removed > n:
            end = mid - 1

        # 목표보다 적은 바위 제거시 거리 늘린다.
        else:
            answer = mid
            start = mid + 1
    return answer


distance = 23
rocks = [3, 6, 9, 10, 14, 17]
n = 2

print(solution(distance, rocks, n))
