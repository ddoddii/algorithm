# Climb stairs
"""
Dynamic Programming - 한칸 이전 + 두 칸 이전 변수 사용해서 최종 값을 빌드해나가기
"""


def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    one_before = 1
    two_before = 1
    total = 0
    for i in range(2, n + 1):
        total = one_before + two_before
        two_before = one_before
        one_before = total
    return total
