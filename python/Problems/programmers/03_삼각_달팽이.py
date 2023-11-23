# 03. 삼각 달팽이
def solution(n):
    snail = [[0] * i for i in range(1,n+1)]
    dy = [1,0,-1]
    dx = [0,1,-1]
    x = y = angle = 0
    num = (n+1)*n // 2
    for i in range(1,num+1):
        snail[y][x] = i
        ny = y + dy[angle]
        nx = x + dx[angle]
        if (ny < n and nx < n and snail[ny][nx] == 0):
            y = ny
            x = nx
        else :
            angle = (angle+1) % 3
            y += dy[angle]
            x += dx[angle]
    return [i for j in snail for i in j]

print(solution(4))