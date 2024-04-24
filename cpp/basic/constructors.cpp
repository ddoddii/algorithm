#include <iostream>
#include <string>
using namespace std;

class User
{
  public:
    string FirstName;
    string LastName;
    int Age;
    string Email;

  public:
    User(string firstName, string lastName, int age, string email)
    {
        FirstName = firstName;
        LastName = lastName;
        Age = age;
        Email = email;
    }

    void getUserInfo()
    {
        cout << "First Name : " << FirstName << endl;
        cout << "Last Name : " << LastName << endl;
        cout << "Age : " << Age << endl;
        cout << "Email : " << Email << endl;
    }
};

int main()
{
    User new_user("ddoddii", "uhm", 25, "test@email.com");
    new_user.getUserInfo();

    return 0;
}