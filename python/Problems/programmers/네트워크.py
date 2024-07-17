from collections import defaultdict


def solution(n, computers):
    dic = defaultdict(list)
    n = len(computers)
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i != j:
                dic[i + 1].append(j + 1)
    visited = [False] * (n + 1)
    cnt = 0

    def dfs(idx):
        if visited[idx]:
            return
        visited[idx] = True
        for n in dic[idx]:
            dfs(n)

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    return cnt


computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 3
print(solution(n, computers))
