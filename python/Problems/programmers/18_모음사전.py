# 모음 사전

# 전체 탐색
def solution(word):
    data = []
    find(data, "", 0)
    for i in range(len(data)):
        if word == data[i]:
            answer = i + 1
    return answer


# 사전 생성
def find(data, p, step):
    if step == 6:
        return
    if p != "":
        data.append(p)
    for vowel in ["A", "E", "I", "O", "U"]:
        find(data, "".join([p, vowel]), step + 1)


word = "EIO"
print(solution(word))
