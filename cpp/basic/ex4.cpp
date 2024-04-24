#include <iostream>
#include <string>
using namespace std;

struct Member
{
    string name;
    string email;
};

class Bookstore
{
  private:
    Member member;

  public:
    Bookstore(string memberName, string memberEmail)
    {
        member.name = memberName;
        member.email = memberEmail;
    }

    void printMember()
    {
        cout << "Member name : " << member.name << "\n"
             << "Member email : " << member.email << endl;
    }
};

int main()
{
    string name, email;
    name = "test";
    email = "test@email.com";
    Bookstore newMember(name, email);
    newMember.printMember();
    return 0;
}