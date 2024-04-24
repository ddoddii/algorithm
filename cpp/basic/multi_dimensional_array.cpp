#include <iostream>
using namespace std;

int main()
{
    int rows, cols;
    cout << "rows, cols : ";
    cin >> rows >> cols;

    int **table = new int *[rows];
    for (int i = 0; i < rows; i++)
    {
        table[i] = new int[cols];
    }
    table[1][2] = 99;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cout << table[i][j] << endl;
        }
    }

    // deallocating
    for (int i = 0; i < rows; i++)
    {
        delete[] table[i];
    }
    delete[] table;
    table = NULL;

    return 0;
}
