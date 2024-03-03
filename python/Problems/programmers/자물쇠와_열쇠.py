# 2020 카카오
# 구현 !!


def solution(key, lock) -> bool:
    holes, kn, ln = 0, len(key), len(lock)
    for i in range(ln):
        for j in range(ln):
            if lock[i][j] == 0:
                holes += 1
    if holes == 0:
        return True

    # rotate 4 times
    for _ in range(4):
        for i in range(-kn + 1, ln):
            for j in range(-kn + 1, ln):
                possible = insert(lock, key, i, j, holes)
                if possible:
                    return True
        newKey = [[0 for _ in range(kn)] for _ in range(kn)]
        for i in range(kn):
            for j in range(kn):
                newKey[i][j] = key[kn - 1 - j][i]
        key = newKey
    return False


def insert(lock, key, x, y, holes) -> bool:
    for i in range(len(key)):
        for j in range(len(key[0])):
            nx, ny = x + i, y + j
            if nx < 0 or ny < 0 or nx >= len(lock) or ny >= len(lock[0]):
                continue
            if key[i][j] == 1:
                if lock[nx][ny] == 1:
                    return False
                holes -= 1
    return holes == 0


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
