/*
Swap Function
• Use pointers to swap the values of two variables.
• Write a function swap(int* a, int* b) that swaps the values of the integers pointed to by a and b.
*/

#include <iostream>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int num1 = 10, num2 = 20;

    std::cout << "Before swap: num1 = " << num1 << ", num2 = " << num2 << std::endl;

    swap(&num1, &num2);

    std::cout << "After swap: num1 = " << num1 << ", num2 = " << num2 << std::endl;

    return 0;
}