def pick3number():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    temp = -1
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                curr = arr[i] + arr[j] + arr[k]
                if curr <= m:
                    temp = max(temp, curr)

    return temp if temp != -1 else -1


print(pick3number())
