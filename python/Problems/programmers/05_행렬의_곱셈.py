# 05. 행렬의 곱셈

def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr2[0])
    middle = len(arr1[0])
    answer = [[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            for k in range(middle):
                answer[i][j] += arr1[i][k]*arr2[k][j]
    return answer
