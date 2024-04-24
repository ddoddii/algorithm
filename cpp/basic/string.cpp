#include <iostream>
#include <string>

using namespace std;

int main()
{
    char a[] = "nocode";
    a[0] = 'd';
    cout << a << endl;
    cout << sizeof(a) << endl;
    cout << strlen(a) << endl;

    const char *b = "nocode"; // b 는 문자열의 주소(b는 스택에 저장), 실제 문자열은 힙의 read-only 에 저장
    cout << b << endl;
    cout << sizeof(b) << endl;
    cout << strlen(b) << endl;

    string c = "nocode";
    cout << c << endl;
    cout << sizeof(c) << endl; // string object 크기 24byte
    cout << c.size() << endl;

    return 0;
}