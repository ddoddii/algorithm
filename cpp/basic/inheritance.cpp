#include <iostream>
using namespace std;

// Abstract class
class Student
{
  public:
    string Name;
    int Age;
    char Gender;
    virtual ~Student()
    {
    }                         // virtual descructor
    virtual void Study() = 0; // virtual method
};

class ProgrammingStudent : public Student
{
    void Study()
    {
        cout << "Learning Programming" << endl;
    }
};

class ArtsStudent : public Student
{
    void Study()
    {
        cout << "Learning Arts" << endl;
    }
};

class MusicStudent : public Student
{
    void Study()
    {
        cout << "Learning Music" << endl;
    }
};

int main()
{
    Student *students[3];
    students[0] = new ProgrammingStudent();
    students[1] = new ArtsStudent();
    students[2] = new MusicStudent();

    for (int i = 0; i <= 2; i++)
    {
        students[i]->Study();
    }

    // delete[] students; -> wrong !!
    for (int i = 0; i <= 2; i++)
    {
        delete students[i];
    }

    return 0;
}