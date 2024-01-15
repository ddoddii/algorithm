def solution(record):
    answer = []
    temp = []
    for r in record:
        temp.append(r.split(" "))
    nickname = dict()
    for i in temp:
        if i[0] == "Enter":
            nickname[i[1]] = i[2]
        elif i[0] == "Change":
            nickname[i[1]] = i[2]
    for i in temp:
        if i[0] == "Enter":
            answer.append(nickname[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(nickname[i[1]] + "님이 나갔습니다.")
    return answer


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
]

print(solution(record))
