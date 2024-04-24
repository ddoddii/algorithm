#include <iostream>
#include <string>
using namespace std;

class Book
{
  public:
    string Title;
    string Author;
    int *Rates;
    int RatesCounter;

    // constructor
    Book(string title, string author)
    {
        Title = title;
        Author = author;
        RatesCounter = 2;
        Rates = new int[RatesCounter];
        Rates[0] = 4;
        Rates[1] = 5;

        cout << Title << " constructor invoked" << endl;
    }

    // destructor - invoked in reverse order
    ~Book()
    {
        delete Rates;
        Rates = nullptr;
        cout << Title << " destructor invoded" << endl;
    }
};

int main()
{
    Book book1("Learning c++", "Barteck Filipek");
    Book book2("Millionaire Fastlane", "M.J");
    return 0;
}