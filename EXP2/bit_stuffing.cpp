#include <iostream>
#include <string>
using namespace std;
int main()
{
    string data;
    cout << "Enter the string: " << endl;
    cin >> data;
    string stuffed;
    int counter = 0;
    for (char ch : data)
    {
        if (ch == '1')
        {
            counter++;
            if (counter == 6)
            {
                stuffed += '0';
                counter = 0;
            }
        }
        else
        {
            counter = 0;
        }
        stuffed += ch;
    };
    cout << "Stuffed String is: " << stuffed << endl;
    return 0;
}
