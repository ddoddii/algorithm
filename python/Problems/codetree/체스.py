import sys

sys.setrecursionlimit(3000)


def chess():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    r, c = map(int, input().split())
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                arr[i][j] = 0
            else:
                move(arr, r - 1, c - 1, n)
    return arr


def move(arr, i, j, n):
    if 0 <= i < n and 0 <= j < n and arr[i][j] == 0:
        arr[i][j] = 1

        move(arr, i + 2, j + 1, n)
        move(arr, i + 2, j - 1, n)
        move(arr, i - 2, j + 1, n)
        move(arr, i - 2, j - 1, n)
        move(arr, i + 1, j + 2, n)
        move(arr, i + 1, j - 2, n)
        move(arr, i - 1, j + 2, n)
        move(arr, i - 1, j - 2, n)


print(chess())
