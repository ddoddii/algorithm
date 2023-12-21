# 돈 거슬러주기 

def solution(money):
    answer = [0] * 9
    divider = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    
    for i in range(9):
        answer[i] = money // divider[i]
        money -= divider[i] * answer[i]
    
    return answer

money = 50237
print(solution(money))