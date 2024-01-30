from heapq import heappush as push, heappop as pop


# 우선순위 큐 사용 (heapq)
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        # 현재 시점에서 작업 가능한 작업 heap 에 추가하기
        for job in jobs:
            if start < job[0] <= now:
                # 우선순위큐에서 배열은 첫번째 원소 기준으로 정렬 -> ([작업시간, 요청시간]이 되게끔 뒤집기)
                push(heap, job[::-1])
        # 처리할 작업이 있으면 처리하고 시간 흐르기
        if len(heap) > 0:
            cur = pop(heap)
            start = now
            now += cur[0]
            i += 1
            answer += now - cur[1]
        # 처리할 작업 없으면 시간 +1 초
        else:
            now += 1

    return answer // len(jobs)


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
