from collections import deque


def solution(n, edge):
    answer = 0
    route = [0] * (n + 1)

    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque()
    q.append(1)
    route[1] = 1

    # 현재 노드에 인접한 노드 탐색 (BFS)
    while q:
        now = q.popleft()
        for g in graph[now]:
            if route[g] == 0:
                route[g] = route[now] + 1
                q.append(g)

    max_distance = max(route)
    for r in route:
        if r == max_distance:
            answer += 1
    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
