def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


# 딕셔너리 사용
def solution2(participant, completion):
    answer = {}
    for i in participant:
        answer[i] = answer.get(i, 0) + 1
    for j in completion:
        answer[j] -= 1
    for k in answer:
        if answer[k]:
            return k


# hash 값 사용
def solution3(participant, completion):
    value = 0
    answer = {}
    for part in participant:
        answer[hash(part)] = part
        value += int(hash(part))
        print(answer)
        print(value)
    for comp in completion:
        value -= int(hash(comp))
    return answer[value]


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution3(participant, completion))
