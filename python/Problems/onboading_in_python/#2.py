#2 암호 해독 - 중복 문자열 삭제

str = "browoanoommnaon"


def solution(str):
    result = []
    i = 0
    while i < len(str):
        if i == len(str)-1 or str[i] != str[i+1]:
            result.append(str[i])
            i += 1
        else:
            i += 2

    result_str = ''.join(result)

    if result_str == str:
        return result_str
    else : 
        return solution(result_str)

print(solution(str))