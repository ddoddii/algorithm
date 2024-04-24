#include <iostream>
using namespace std;

int add(int a, int b)
{
    return a + b;
}

double add(double a, double b)
{
    return a + b;
}

void problem1()
{
    int a, b;
    cout << "a,b :  ";
    cin >> a >> b;
    double c, d;
    cout << "c,d : ";
    cin >> c >> d;
    cout << endl;
    cout << "a+b: " << add(a, b) << endl;
    cout << "c+d: " << add(c, d);
}

void func1(int a, int b)
{
    cout << "func1 : " << a + b << endl;
}

void func2(int *a, int *b)
{
    int sum = *a + *b;
    cout << "func2 : " << sum << endl;
}

void problem2()
{
    int a = 3;
    int b = 8;
    func1(a, b);
    func2(&a, &b);
}

int func3(int *ptr, int size)
{
    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum = sum + ptr[i];
        ptr[i] = 0;
    }
    return sum;
}

void problem3()
{
    int a[5] = {1, 2, 3, 4, 5};
    int sum = func3(a, 5);
    cout << "sum : " << sum << endl;

    for (int i = 0; i < 5; i++)
    {
        cout << *(a + i) << endl;
    }
}

int main()
{
    // problem1();
    // problem2();
    problem3();

    return 0;
}