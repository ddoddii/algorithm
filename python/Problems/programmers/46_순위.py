from collections import defaultdict


def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)

    for winner, loser in results:
        win[loser].add(winner)
        lose[winner].add(loser)

    for i in range(1, n + 1):
        for winner in win[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            win[loser].update(win[i])

    for i in range(1, n + 1):
        count = 0
        count += len(win[i])
        count += len(lose[i])
        if count == n - 1:
            answer += 1
    return answer


# 그래프 - 플로이드 워셜 기법
def solution2(n, results):
    answer = 0
    total = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        total[i][i] = -1
    for result in results:
        total[result[0] - 1][result[1] - 1] = "WIN"
        total[result[1] - 1][result[0] - 1] = "LOSE"
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == "WIN" and total[k][j] == "WIN":
                    total[i][j] = "WIN"
                elif total[i][k] == "LOSE" and total[k][j] == "LOSE":
                    total[i][j] = "LOSE"
    for i in total:
        if 0 not in i:
            answer += 1
    return answer
