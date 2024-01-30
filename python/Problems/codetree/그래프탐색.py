n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
answer = 0


def graphSearch():
    for _ in range(m):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    visited[1] = True
    dfs(1)
    return answer


def dfs(node):
    global answer
    for curr in graph[node]:
        if not visited[curr]:
            visited[curr] = True
            answer += 1
            dfs(curr)


print(graphSearch())
