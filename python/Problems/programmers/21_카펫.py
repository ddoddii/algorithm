# 완전 탐색
"""
세로가 더 작으니 더 작은 범위를 완전 탐색하자 !
완전 탐색 할 때는 최소, 최대 범위를 고민해보자.
"""


def solution(brown, yellow):
    grid = brown + yellow
    # n : 세로 길이, m : 가로 길이 (직사각형 : 가로 > 세로)
    for n in range(3, int(grid ** 0.5) + 1):
        if grid % n != 0:
            continue
        m = grid // n
        if (m - 2) * (n - 2) == yellow:
            return [m, n]


print(solution(10, 2))
