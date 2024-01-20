def solution(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]

    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(0, i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j] + triangle[i][j], dp[i - 1][j - 1] + triangle[i][j]
                )
    return max(dp[-1])


"""
- 전체를 저장하지 않고 풀이
- 마지막에서 시작해서 위로 올라오기
"""


def solution2(triangle):
    height = len(triangle) - 1
    while height > 0:
        for i in range(height):
            triangle[height - 1][i] += max(triangle[height][i], triangle[height][i + 1])
        height -= 1
    return triangle[0][0]


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution2(triangle))
