/*
smart pointer : wrapper for raw pointer
deallocate memory automatically
- unique pointer : cannot be shared
- shared pointer
- weak pointer
*/

#include <iostream>
#include <memory>
using namespace std;

class MyClass
{
  public:
    MyClass()
    {
        cout << "Constructor invoked" << endl;
    }
    ~MyClass()
    {
        cout << "Destructor invoked" << endl;
    }
};

int main()
{
    unique_ptr<int> unPtr1 = make_unique<int>(25);
    cout << *unPtr1 << endl; // 25

    unique_ptr<int> unPtr2 = std::move(unPtr1); // move unPtr1 -> unPtr2
    cout << *unPtr2 << endl;                    // 25
    // cout << *unPtr1 << endl; // unPtr- null pointer, exception !!

    shared_ptr<MyClass> shPtr1 = make_shared<MyClass>();
    cout << "Shared count " << shPtr1.use_count() << endl;
    shared_ptr<MyClass> shPtr2 = shPtr1;
    cout << "Shared count " << shPtr2.use_count() << endl;

    weak_ptr<int> wkPtr1;
    {
        shared_ptr<int> shPtr = make_shared<int>(50);
        wkPtr1 = shPtr;
    }
    // cout << "Weak pointer " << wkPtr1 << endl; -> error ! (weak pointer is null)
    return 0;
}