## Review <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Snake.png" alt="Snake" width="25" height="25" />

<details>
    <summary><h3>python 에서 mutable, immutable</h3></summary>

```python
grid = [1, 2, 3]

def function(grid):
    visited = [0] * len(grid)
    visit = 1

    def nested_function():
        visited[0] = 1
        visit += 1

    nested_function()
    return visit, visited
```
위의 함수를 실행하면 `UnboundLocalError: local variable 'visit' referenced before assignment` 에러가 뜹니다. list 타입인 visited 는 변경 가능한데, 왜 visit 는 nested function 에서 접근해서 수정할 수 없을까요? 

객체의 Mutable / Immutable 과 Scope 에 대해 정확히 구분해야 합니다. 

#### Mutable vs. Immutable 

- **Mutable** : list, dictionary, set 는 생성 후 변경할 수 있습니다. mutable object 를 수정하면 오브젝트 자체를 변경하는 것입니다.
- **Immutable** : integer, float, string, tuple 은 생성 후 변경할 수 없습니다. 수정 시에 원본 객체를 수정하는 것이 아니라 새로운 오브젝트가 만들어집니다. 

#### Scope

- **Nested Function Scopes** : 함수를 함수 내부에 정의하면, 안에 있는 함수는 바깥 함수에 정의되어 있는 변수들에 접근할 수 있습니다. 접근은 가능하지만 수정은 불가능합니다. 

위의 예시에서, `visited` 는 리스트 이며, **mutable** 오브젝트입니다. nested_function() 안에 있는 `visited[0] = 1` 는 리스트를 수정합니다. 중요한 점은 리스트를 수정한다는 것은, 리스트는 mutable 오브젝트이므로 리스트 오브젝트 자체를 수정하는 것이 아니라, 오브젝트는 그대로 두고 '값'만 수정하는 것이기 때문에 visited 는 수정할 수 있습니다. 

`visit += 1` 는 `visit` 에 1을 더함으로써 값을 수정하고자 합니다. 하지만 `visit` 변수는 integer 로, **immutable** 오브젝트입니다. 파이썬은 integer 를 수정할 때, 새로운 값을 가지는 새로운 오브젝트를 생성합니다. 따라서 새로운 로컬 변수 `visit` 를 생성하려 하는데, 이 로컬 변수 `visit` 가 할당되지 않았으므로 `UnboundLocalError`가 발생합니다. 

이 문제를 해하려면, 아래와 같이 수정하면 visit 를 nested_function 에서도 접근하여 수정할 수 있습니다. `nonlocal visit` 를 선언해줌으로써, nested_function 안에서 새로운 `visit` 변수를 생성하는 것이 아니라, 바깥에 있는 visit 를 나타내는 것이라고 알려줄 수 있습니다. 

```python
def solution(grid):
    visited = [0] * len(grid)
    visit = 1

    def sub_function():
        nonlocal visit
        visited[0] = 1
        visit += 1

    sub_function()
    return visit, visited
```

</details>

<details>
    <summary><h3>python list slicing</h3></summary>

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7]
print(nums[2:]) # [2, 3, 4, 5, 6, 7]
print(nums[-2:]) # [6, 7] (뒤에서 2번째 인덱스 이상)
print(nums[:2]) # [0, 1] (앞에서 2번째 인덱스 미만)
print(nums[:-2]) # [0, 1, 2, 3, 4, 5] (뒤에서 2번째 인덱스 미만)
print(nums[1:5:3]) # [1, 4] (인덱스1 이상 5미만 중 간격 3)
print(nums[::-1]) # [7, 6, 5, 4, 3, 2, 1, 0] (거꾸로 뒤집기)
print(nums[::-2]) # [7, 5, 3, 1] (뒤집는데 간격 2)
 

# nums rotate by k
k = 2
nums[:] = nums[-k:] + nums[:-k]
print(nums) # [6, 7, 0, 1, 2, 3, 4, 5]
```


</details>

<details>
    <summary><h3>Bitwise opreation</h3></summary>

- **AND(&)**
  - `AND` : 두 비트가 모두 1일 때만 1
  - a ^ a = 1

    ```python
    a = 6  # 110
    print(a & 1) # 0 (& : AND -> 1 & 1 인 경우만 1, 가장 마지막 비트가 1인 경우만 1)
    a >>= 1 # >>1 : 나누기 2^1 = shift right
    print(a & 1) # 1 
    a >>= 1
    print(a & 1) # 1
    ```

- **XOR(^)**
  - `XOR` : 두 비트가 다를때만 1
  - a ^ a = 0, a ^ 0 = a, a ^ b ^ a = b (XOR는 교환, 결합법칙 성립)
  
    ```python
    x, y = 8, 10 # x = 1000, y = 1010
    x ^= y # XOR : 두 비트가 다르면 1, x = 0010 // x = x^y
    print(x) # 2 
    y ^= x # XOR : 두 비트가 다르면 1, y = 1000  // y = y^x = y^x^y = x : 교환됨 
    print(y) # 8
    x ^= y # XOR : x = 1010 // x = x^y = x^y^x = y : 교환됨
    print(x) # 10
    ```

- **OR(|)**
  - `OR` : 두 비트 중 1개만 1이면 1, 두 비트 모두 0일때만 0

- **Shift Left(<<)**
  - `A << B` : A를 B비트만큼 왼쪽으로 밀기
  - `a << 2` : a * (2^2)

- **Shift Right(>>)**
  - `A >> B` : A를 B비트만큼 오른쪽으로 밀기
  - `a >> 2` : a / (2^2)


</details>


<details>
    <summary><h3>유용한 string 관련 함수</h3></summary>

- `A.startswith(B) -> Boolean` : A가 B문자열로 시작하는지 반환

</details>

<details>
    <summary><h3>Backtracking Tip</h3></summary>

"Compute All", "Exhaust All" may imply it is a backtracking problem.

- **choices**
  - core choices we make each step
  - what decision space can we choose from?
- **constraints**
  - what limited space do we need to validate? (ex. sudocu - same col/row)
  - if this is valid, we recurse on our decision
- **goals**
  - what is our base case?

```c
void Backtrack(res,args)
  if (GOAL REACHED)
    add solution to res
    return 

  // Explore all choices
  for (int i=0; i < NUMBER_OF_CHOICES; i++)
    if (CHOICES[i] is valid) 
      make choices[i]
      Backtrack(res, args)
      undo choices[i]
```


</details>

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