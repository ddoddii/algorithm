from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

counter = Counter(arr)

for t in target:
    if counter[t] > 0:
        print(1)
    else:
        print(0)

n = 5
arr = [4, 1, 5, 2, 3]
m = 5
target = [1, 3, 7, 9, 5]
