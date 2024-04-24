#include <iostream>
using namespace std;

/*
Copy constructor
- Custom Copy constructor 를 만들어줘야한다!
- 특히 포인터 관련 변수(배열)은 새로운 배열을 만들고 값을 옮겨줘야 한다.
*/

class Book
{
  public:
    string Title;
    string Author;
    float *Rates;
    int RatesCounter;

    Book(string title, string author)
    {
        Title = title;
        Author = author;

        RatesCounter = 2;
        Rates = new float[RatesCounter];
        Rates[0] = 5;
        Rates[1] = 4;
    }

    ~Book()
    {
        delete[] Rates;
        Rates = nullptr;
    }

    // Custom Copy Constructor
    Book(const Book &original)
    {
        Title = original.Title;
        Author = original.Author;
        // Rates = original.Rates; -> delete 시 문제가 생긴다.
        RatesCounter = original.RatesCounter;

        Rates = new float[RatesCounter];
        for (int i = 0; i < RatesCounter; i++)
        {
            Rates[i] = original.Rates[i];
        }
    }
};

void printBook(Book book)
{
    cout << "Title : " << book.Title << endl;
    cout << "Author : " << book.Author << endl;

    float sum = 0;
    for (int i = 0; i < book.RatesCounter; i++)
    {
        sum += book.Rates[i];
    }
    cout << "Avg Rage : " << sum / book.RatesCounter << endl;
}

int main()
{
    Book book1("Millionaire Fastlane", "M.J");
    Book book2("Learn c++", "Bartek F.");
    Book book3(book1);  // copy constructor
    Book book4 = book2; // copy constructor (creating object based on already existing object)

    printBook(book3);
    printBook(book4);

    return 0;
}