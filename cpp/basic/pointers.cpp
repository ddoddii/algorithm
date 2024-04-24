/*
Pointer Basics
- Create an integer variable and define a pointer to that variable.
- Assign the variable's address to the pointer, and then use the pointer to modify the value of the variable.
- Check the modified value
*/

#include <iostream>
#include <string>
using namespace std;

void pointerBasics()
{
    int num = 10;
    cout << "Initial value: " << num << endl;

    // Define a pointer to the variable (pointer type = variable type)
    int *numPtr = &num;

    cout << "Pointer address : " << numPtr << endl;

    cout << "Value inside pointer : " << *numPtr << endl;

    // Use the pointer to modify the value of the variable
    *numPtr = 20;

    // Check the modified value
    cout << "Modified value: " << num << endl;
}

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

void arrayPointers()
{
    int luckyNumbers[5] = {1, 2, 3, 4, 5};
    cout << luckyNumbers << endl;        // 0x16b0e69a0 (포인터, 배열의 첫번째 원소의 주소값)
    cout << &luckyNumbers[0] << endl;    // 0x16d1929a0
    cout << luckyNumbers[2] << endl;     // 3
    cout << *(luckyNumbers + 2) << endl; // 3

    int anotherNumbers[5]; // 0x16f04298c (포인터)
    cout << anotherNumbers << endl;
    for (int i = 0; i < 5; i++)
    {
        // cout << "Number : ";
        //  cin >> anotherNumbers[i];
    }
    for (int i = 0; i < 5; i++)
    {
        cout << *(anotherNumbers + i) << endl;
    }
}

int getMin(int numbers[], int size)
{
    int min = numbers[0];
    for (int i = 1; i < size; i++)
    {
        if (numbers[i] < min)
        {
            min = numbers[i];
        }
    }
    return min;
}

int getMax(int numbers[], int size)
{
    int max = numbers[0];
    for (int i = 1; i < size; i++)
    {
        if (numbers[i] > max)
        {
            max = numbers[i];
        }
    }
    return max;
}

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
    cout << "Min is " << min << endl;
    cout << "Max is " << max << endl;
}

int main()
{
    pointerBasics();
    voidPointers();
    arrayPointers();
    functionPointers();
    return 0;
}