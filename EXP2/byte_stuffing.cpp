#include <iostream>
#include <string>
using namespace std;
int main()
{
    char s, e;
    cout << "Enter the start char: ";
    cin >> s;
    cout << "Enter the end char: ";
    cin >> e;
    char escape;
    cout << "Enter the escape char: ";
    cin >> escape;
    string data;
    cout << "Enter the data: ";
    cin >> data;
    string stuffed;
    stuffed += s;
    for (char ch : data)
    {
        if (ch == s || ch == e || ch == escape)
        {
            stuffed += escape;
        }
        stuffed += ch;
    }
    stuffed += e;
    cout << "Stuffed String is: " << stuffed << endl;
    return 0;
}