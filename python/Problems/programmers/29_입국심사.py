# 이진 탐색
"""
- 심사대에 사람을 줄 세우는 대신, 시간을 기준으로 몇명을 처리할 수 있는지 접근
- 최소 시간 : 1, 최대 시간 : max(times) * n
- 처리할 수 있는 사람 수와 n 을 비교해서 이진탐색
"""


def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
            # 사람 수가 n 보다 많아지면 더 이상 time 반복문 돌지 않고 탈출 (시간 절약)
            if people >= n:
                break
        # 처리할 수 사람 수가 n 보다 많아짐 = 시간 과다 -> mid 의 왼쪽 탐색
        if people >= n:
            answer = mid
            right = mid - 1
        # 처리할 수 사람 수가 n 보다 적어짐 = 시간 부족 -> mid 의 오른쪽 탐색
        elif people < n:
            left = mid + 1
    return answer


n = 6
times = [7, 10]
print(solution(n, times))
