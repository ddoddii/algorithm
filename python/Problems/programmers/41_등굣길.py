# [y][x] 표기 주의
def solution(m, n, puddles):
    MOD = 1000000007
    grid = [[1 for _ in range(m)] for _ in range(n)]
    # 웅덩이 마킹
    for puddle in puddles:
        [y, x] = puddle
        grid[x - 1][y - 1] = 0

    # 첫번째 열 , 행 초기화 (웅덩이 이후에는 0)
    for i in range(1, n):
        if grid[i][0] == 0 or grid[i - 1][0] == 0:
            grid[i][0] = 0
    for j in range(1, m):
        if grid[0][j] == 0 or grid[0][j - 1] == 0:
            grid[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] == 0:
                continue
            grid[i][j] = (grid[i - 1][j] + grid[i][j - 1]) % MOD
    return grid[-1][-1] % MOD


def solution2(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for y in range(n):
        for x in range(m):
            if ([x + 1, y + 1] in puddles) or ((y, x) == (0, 0)):
                continue
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD
    return dp[-1][-1]


m, n, puddles = 4, 3, [[2, 2]]
print(solution2(m, n, puddles))
