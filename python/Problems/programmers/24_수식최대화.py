import re
from itertools import permutations

"""
- 연산의 우선 순위를 지정(순열 이용 -> *,-,+ 니까 6가지이다.) -> 후위 표기법 활용
- expression 자를 때는 정규표현식 이용 (숫자 \d+)

< 후위 표기법 규칙>
1. 숫자는 그대로 출력한다.
2. 만약 스택이 비어있다면 연산자를 그냥 스택에 넣는다.
3. (스택의 top에 있는 연산자의 우선순위 < 현재 연산자의 우선순위) 이면 현재 연산자를 그냥 스택에 넣는다.
4. (스택의 top에 있는 연산자의 우선순위 >= 현재 연산자의 우선순위) 이면 2번 혹은 3번 상황이 될 때까지 pop 하여 출력하고 연산자를 스택에 넣는다.
5. 모든 수식을 다 사용했다면 스택이 빌 때까지 pop하여 출력한다.

<후위 표기법 사칙연산>
1. 숫자는 스택에 그냥 추가한다.
2. 연산자가 나오면 숫자 2개를 pop 해서 계산한다.
3. 이때 먼저 pop 되는 숫자가 두 번째 값, 나중에 pop되는 숫자가 첫 번째 값으로 하여 계산해야 한다. 계산한 값은 다시 스택에 넣는다.
"""

# 후위 표기법으로 변환
def toPostFix(tokens, priority):
    stack = []  # 연산자 저장 스택
    postfix = []  # 후위 표기법 저장
    for token in tokens:
        # 숫자면 바로 postfix 저장
        if token.isdigit():
            postfix.append(token)

        else:
            # stack 이 비어있으면 연산자 추가
            if not stack:
                stack.append(token)
            else:
                # 연산자 우선순위 비교 (규칙3 - )
                while stack and priority[token] <= priority[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix


# 후위 표기법 계산
def calc(tokens):
    stack = []  # 숫자 스택
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
            continue
        # 연산자가 나오면 숫자 2개를 pop 해서 계산
        num1 = stack.pop()
        num2 = stack.pop()
        if token == "*":
            stack.append(num1 * num2)
        elif token == "+":
            stack.append(num1 + num2)
        elif token == "-":
            # 뺄셈은 순서 중요 -> num1 이 나중 숫자, num2 가 먼저 오는 숫자
            stack.append(num2 - num1)
    return stack.pop()


def solution(expression):
    answer = 0
    operators = ["-", "+", "*"]
    tokens = re.split(r"([-+*])", expression)
    # priority 만들기
    for i in map(list, permutations(operators)):
        priority = {o: p for p, o in enumerate(list(i))}
        postfix = toPostFix(tokens, priority)
        answer = max(answer, abs(calc(postfix)))
    return answer


exp = "50*6-3*2"
print(solution(exp))
