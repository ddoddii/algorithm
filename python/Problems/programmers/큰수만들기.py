from itertools import combinations


# 그리디 -> 스택 사용하자
def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    stack = stack[:-k] if k else stack
    return "".join(stack)


number = "2104"
k = 1
print(solution(number, k))
