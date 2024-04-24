#include <iostream>
#include <string>
using namespace std;

void compareStringLength()
{
    string s1, s2;
    cout << "string 1, string 2 : ";
    cin >> s1 >> s2;
    if (s1.length() < s2.length())
    {
        cout << s2 << endl;
    }
    else
    {
        cout << s1 << endl;
    }
}

void concatenatingNames()
{
    string first, last;
    cout << "first, last name :";
    cin >> first >> last;
    cout << "full name : " << first + last << endl;
}

int main()
{
    compareStringLength();
    concatenatingNames();
    return 0;
}