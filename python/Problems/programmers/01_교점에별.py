# 01. 교점에 별 만들기
def solution(line):
    answer = []
    n = len(line)
    poses = []
    for i in range(n):
        a,b,e = line[i]
        for j in range(i+1,n):
            c,d,f = line[j]
            if a*d == b*c : continue
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            # 정수이면 교점에 추가
            if (x == int(x) and y == int(y)):
                x = int(x)
                y = int(y)
                poses.append([x,y])
    x_min , y_min, x_max, y_max = int(1e15) , int(1e15), -int(1e15), -int(1e15)
    for pos in poses:
        if pos[0] < x_min : x_min = pos[0]
        if pos[0] > x_max : x_max = pos[0]
        if pos[1] < y_min : y_min = pos[1]
        if pos[1] > y_max : y_max = pos[1]

    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.'] * x_len for _ in range(y_len)]

    for star_x, star_y in poses:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = '*'

    for result in coord:
        answer.append(''.join(result))
    
    return answer[::-1];

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
