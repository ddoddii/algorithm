## Review  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Animals/Spouting%20Whale.png" alt="Spouting Whale" width="30" height="30" />


<details>
    <summary><h3>Pointers</h3></summary>

### Pointers

- 포인터 : 변수의 메모리 주소
- 포인터도 "타입"이 있다. (int 에 대한 포인터, double 에 대한 포인터...)
- 포인터도 다른 변수들 처럼 선언된다.
  - 변수 앞에 "*" 붙이기
  - `int *p1, *p2, v1, v2;` -> p1,p2 : 포인터, v1,v2 : int 변수
- `p1 = &v1` : p1 은 v1 변수를 포인트 한다 = p1 은 v1의 주소이다.
- '&' : 변수의 주소 반환
  - call-by-reference
  - `int *numPtr = &num;`
- '*' : dereference 포인터
  - `cout << *p1` : p1 이 포인트하고 있는 데이터 출력해줘 
- 포인터끼리 할당할 수 있다.

    ```cpp
    int *p1, *p2;
    p2 = p1; // "p2가 포인트하는 곳을 p1이 포인트하는 곳으로 바꿔줘"
    *p2 = *p1 // "p2가 포인트하는 변수의 값을 p1이 포인트하는 변수의 값으로 바꿔줘"
    ```

```cpp
void pointerBasics()
{
    int num = 10;
    cout << "Initial value: " << num << endl;

    // Define a pointer to the variable (pointer type = variable type)
    int *numPtr = &num; // & : 변수의 주소 반환

    cout << "Pointer address : " << numPtr << endl; //  0x16d3669bc (실제 주소)

    cout << "Value inside pointer : " << *numPtr << endl; // 10 (주소에 저장되어 있는 실제 값)

    // Use the pointer to modify the value of the variable
    *numPtr = 20;

    // Check the modified value
    cout << "Modified value: " << num << endl; // 20 (실제 값이 바뀜)
}
```

### Void pointers

```cpp
// void pointer - store address of any data type
void print(void *ptr, char type)
{
    switch (type)
    {
    case 'i':
        cout << *((int *)ptr) << endl;
        break;
    case 'c':
        cout << *((char *)ptr) << endl;
        break;
    }
}

void voidPointers()
{
    int number = 5;
    char letter = 'a';
    print(&number, 'i');
    print(&letter, 'c');
}
```

- 어느 데이터 타입의 주소든 저장할 수 있다.

### New operator
- 변수를 동적으로 할당할 수 있다. 
- `int *p1 = new int;`
  - 이름없는 변수를 만들고, p1은 그 변수를 가리킨다. 


### Return multiple values from a function using pointers

```cpp
void getMinAndMax(int numbers[], int size, int *min, int *max)
{
    for (int i = 1; i < size; i++)
    {
        if (numbers[i] > *max)
        {
            *max = numbers[i];
        }
        if (numbers[i] < *min)
        {
            *min = numbers[i];
        }
    }
}

void functionPointers()
{
    int numbers[5] = {5, 4, -2, 29, 6};
    int min = numbers[0];
    int max = numbers[0];
    getMinAndMax(numbers, 5, &min, &max); // pass a address
    cout << "Min is " << min << endl; // -2
    cout << "Max is " << max << endl; // 29
}
```

- `getMinAndMax` 함수에 min,max 변수의 주소를 넘겨준다. 그러면 `getMinAndMax` 함수 내에서 변경된 값을 바로 functionPointers() 함수에서 접근할 수 있다.

### Delete

- 동적 메모리를 할당해제 한다. 즉, 포인터 p가 가리키고 있던 동적 메모리를 할당 해제한다. 
- `delete p` 를 하면, 메모리는 사라지지만 p는 여전히 그곳을 가리킨다(dangling pointer). 이것을 해결하려면 `p = NULL` 을 명시해줘야 한다. 

</details>


<details>
    <summary><h3>Arrays</h3></summary>

### Static Arrays

- 고정된 크기의 배열
- 메모리의 연속된 주소에 저장되므로, 각 원소에 접근하는 시간이 매우 빠르다.
- 하지만 프로그램 컴파일 전에 사이즈가 결정되어야 한다. 

```cpp
int main()
{
    int myArray[5];
}
```

### Dynamic Arrays

- 프로그램 실행 시 크기가 정해진다. 
- `new` 를 사용해서 만든다.
- Dynamic Arrays는 런타임시 동적으로 할당되므로, 런타임에 소멸시켜야 한다. 

    ```cpp
    d = new double[10];
    delete[] d;
    d = NULL;
    ```

```cpp
int main()
{
    int size;
    cout << "size : ";
    cin >> size;
    int *myArray = new int[size]; // size allocated at runtime

    for (int i=0; i<size ; i++) {
        cout << "Array[" <<i << "] ";
        cin >> myArray[i]
    }

    for (int i=0; i<size ; i++) {
        // cout << myArray[i] << " ";
        cout << *(myArray+i) << " ";
    }

    delete[] myArray; // memory deallocation
    myArray = NULL; // prevent pointer dangling
}
```

### Pointers & Arrays

```cpp
void arrayPointers()
{
    int luckyNumbers[5] = {1, 2, 3, 4, 5};
    cout << luckyNumbers << endl;        // 0x16b0e69a0 (포인터, 배열의 첫번째 원소의 주소값)
    cout << &luckyNumbers[0] << endl;    // 0x16d1929a0
    cout << luckyNumbers[2] << endl;     // 3
    cout << *(luckyNumbers + 2) << endl; // 3

    int anotherNumbers[5]; // 0x16f04298c (배열 변수는 첫번째 인덱스 변수를 가리킴 - 일종의 포인터 변수)
    cout << anotherNumbers << endl;
    for (int i = 0; i < 5; i++)
    {
        cout << "Number : ";
        cin >> anotherNumbers[i];
    }
    for (int i = 0; i < 5; i++)
    {
        cout << *(anotherNumbers + i) << endl;
    }

    int a[10];
    typedef int* IntPtr;
    IntPtr p;
    p = a; // legal
    a = p; // illegal !! (array pointer 는 CONSTANT 포인터임)
}
```

- array pointer 는 CONSTANT 포인터이다. 
- array 변수는 `const int*` 타입이다.

### Multi-dimensional Arrays


</details>

