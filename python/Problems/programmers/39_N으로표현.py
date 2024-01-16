"""
- ex) i = 4 (숫자 N 4개 사용시)
- 숫자 1개 사용한 결과 * 숫자 3개 사용한 결과, 숫자 2개 사용결과 * 숫자 2개 사용결과 ... 
- 단순 전전 dp, 전 dp 만 활용해서는 안된다. 
- 처음부터 (i = 1) 부터 모두 계산해야 한다.
- 그래서 for loop 을 3번 사용
"""

def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1, len(dp)):
        case = dp[i]
        case.add(int(str(N)*i))
        for j in range(1,i):
            for k in dp[j]:
                for l in dp[i-j]:
                    case.add(k+l)
                    case.add(k-l)
                    case.add(k*l)
                    if l != 0 and k != 0 : case.add(k//l)
        if number in case: return i
    return -1

N = 5
number = 12

dp = [set() for i in range(9)]
dp[0].add(N)
for i in range(1, len(dp)):
    case = dp[i]
    case.add(int(str(N)*i))
    for j in range(1,i):
        for k in dp[j]:
            for l in dp[i-j]:
                case.add(k+l)
                case.add(k-l)
                case.add(k*l)
                if l != 0 and k != 0 : case.add(k//l)
    if number in case:
        print(i)    