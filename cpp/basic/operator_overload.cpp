#include <iostream>
#include <list>
#include <string>
using namespace std;

struct YoutubeChannel
{
    string Name;
    int SubscribersCount;
    YoutubeChannel(string name, int subscribersCount)
    {
        Name = name;
        SubscribersCount = subscribersCount;
    }

    bool operator==(const YoutubeChannel &channel) const
    {
        return this->Name == channel.Name;
    }
};

// << operator overload, global function
// 여러 개 프린트하기 위해 ostream 반환
ostream &operator<<(ostream &COUT, YoutubeChannel &ytChannel)
{
    COUT << "Name : " << ytChannel.Name << endl;
    COUT << "Subscribers : " << ytChannel.SubscribersCount << endl;
    return COUT;
}

struct MyCollection
{
    list<YoutubeChannel> myChannels;
    // member function
    void operator+=(YoutubeChannel channel)
    {
        this->myChannels.push_back(channel);
    }

    void operator-=(YoutubeChannel channel)
    {
        this->myChannels.remove(channel);
    }
};

ostream &operator<<(ostream &COUT, MyCollection &myCollection)
{
    for (YoutubeChannel ytChannel : myCollection.myChannels)
    {
        COUT << ytChannel << endl;
    }
    return COUT;
}

int main()
{
    YoutubeChannel yt1 = YoutubeChannel("ddoddii", 5);
    YoutubeChannel yt2 = YoutubeChannel("second channel", 10);

    // cout << yt1 << yt2;

    MyCollection myCollection;
    myCollection += yt1;
    myCollection += yt2;
    myCollection -= yt1;
    cout << myCollection;
    return 0;
}