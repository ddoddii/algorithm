#08. 튜플

def solution(s):
    data = s[2:-2].split("},{")
    data = sorted(data, key = lambda x : len(x))
    answer = []
    for item in data:
        item = list(map(int, item.split(',')))
        for value in item:
            if value not in answer:
                answer.append(value)
    return answer

def solution2(s):
    answer = {}
    s = sorted(s[2:-2].split("},{"), key = len)
    for tuples in s:
        elements = tuples.split(',')
        for element in elements:
            number = int(element)
            answer[number] = 1
    return list(answer)

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = sorted(s[2:-2].split("},{"), key = len)
print(s)