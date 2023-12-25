# 12. 이진 변환 반복하기

def solution(s):
    total_zeros = 0
    time = 0
    while s != '1':
        zeros = s.count('0')
        length = len(s) - zeros
        s = format(length,'b')
        time += 1
        total_zeros += zeros

    return [time, total_zeros]

s =	"1111111"
print(solution(s))
