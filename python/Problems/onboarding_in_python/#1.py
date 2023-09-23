#1. 책 페이지 비교를 통해 이긴 사람 구하기 


def solution(pobi, crong):
    if pobi[0] % 2 != 1 or (pobi[1] - pobi[0]) != 1 or pobi[1] % 2 != 0 :
        return -1
    if crong[0] % 2 != 1 or (crong[1] - crong[0]) != 1 or crong[1] % 2 != 0 :
        return -1 

    pobi_score = calculate_score(pobi)
    crong_score = calculate_score(crong)
    
    if pobi_score > crong_score:
        return 1
    if crong_score > pobi_score:
        return 2
    else :
        return 0
    

def calculate_score(pages):
    sums = []
    muls = []
    
    for page in pages:
        N = [int(i) for i in str(page)]
        sums.append(sum(N))
        mul = 1
        for num in N:
            mul *= num
        muls.append(mul)
        
    max_sum = max(sums)
    max_mul = max(muls)
    score = max(max_sum, max_mul)
    
    return score 

pobi = [99, 132]
crong = [211, 212]


print(solution(pobi,crong))
    