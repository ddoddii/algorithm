#include <iostream>
using namespace std;

class MenuItem
{
  public:
    string name;
    MenuItem()
    {
        name = "unknown";
        cout << "Base class default constructor" << endl;
    }

    MenuItem(string set_name)
    {
        name = set_name;
        cout << "Base class Param constructor" << endl;
    }
};

class Drink : public MenuItem
{
  public:
    double ounces;
    using MenuItem::MenuItem;
    Drink()
    {
        ounces = 8;
        cout << "Derived class default constructor" << endl;
    }

    Drink(double set_ounces) : MenuItem("n/a")
    {
        ounces = set_ounces;
        cout << "Derived class Param constructor" << endl;
    }
};

int main()
{
    Drink hot_chocolate("hot chocolate");
    return 0;
}