"""
- two pointer
- 어떻게 옮길지 기준을 잘 잡기 !!
"""


def solution(gems):
    kind = len(set(gems))
    size = len(gems)
    answer = [0, size - 1]
    dic = {gems[0]: 1}
    left, right = 0, 0
    while right < size:
        # 모든 종류가 안채워졌으면 오른쪽으로 확장
        if len(dic) < kind:
            right += 1
            if right == size:
                break
            dic[gems[right]] = dic.get(gems[right], 0) + 1
        # 모든 종류가 채워졌으면 왼쪽으로 줄이기 (len(dic) == kind)
        else:
            if (right - left + 1) < (answer[1] - answer[0] + 1):
                answer = [left, right]
            if dic[gems[left]] == 1:
                del dic[gems[left]]
            else:
                dic[gems[left]] -= 1
            left += 1
    return [answer[0] + 1, answer[1] + 1]


gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))

print(format(int("111"), "x"))
print(int("111", 2))
