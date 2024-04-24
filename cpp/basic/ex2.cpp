#include <iostream>
using namespace std;

void problem3()
{
    int N;
    cout << "N : ";
    cin >> N;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 0; j < i; j++)
        {
            cout << '*';
        }
        cout << endl;
    }
}

int main()
{
    problem3();
}