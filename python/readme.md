## Review 👀

### 배열
- 행렬 내 탐색 문제는 방향을 설정해보자. 위[-1,0],아래[1,0],오른쪽[0,1], 왼쪽[0,-1] 
- x축 뱡향 : col, y축 방향 : row -> arr[y][x]
- 배열 out of index error 항상 생각

### 문자열
- 람다식 활용
    `data = sorted(data, key = lambda x : len(x))`
- list(map) 활용
    `list(map(int, item.split(',')))`

### Walrus assignment
:=을 기준으로
1. 왼쪽에 있는 변수(variable)에
2. 오른쪽의 표현(expression)을
3. 값(value)으로써
4. 할당(assignment)함과 동시에
5. 표현(expression)으로써의 기능을 수행하게 해준다.

```python
a = "안녕하세요 저는 Readme입니다"
if (n := len(a)) > 10:
    print(sentence := f"Sentence is {n} long, longer than 10)")
print(n, sentence)
# 18 Sentence is 18 long, longer than 10)
```



## Algorithm Study 
1. Linked Lists
2. Doubly Linked Lists
3. Stacks & Queues
4. Trees
5. Hash Tables
6. Graphs
7. Heaps
8. Recursion
9. Recursive Binary Search Trees
10. Basic Sorts
11. Merge Sort
12. Quick Sort
13. Tree Traversal

## 학습 자료
- Python Data Structures & Algorithms , Udemy
- Leetcode excersises 
- Programmers