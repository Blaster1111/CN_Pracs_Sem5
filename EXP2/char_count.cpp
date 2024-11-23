#include <iostream>
#include <vector>
#include<string.h>
using namespace std;
int main()
{
    vector<string> frames;
    int n;
    cout << "Enter the number fo frames" << endl;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "Enter the " << i << "th frame" << endl;
        string temp;
        cin >> temp;
        frames.push_back(temp);
    }
    string stuffed = "";
    for (auto &frame : frames)
    {
        int size = frame.size();
        size++;
        stuffed += to_string(size) + frame;
    }
    cout << "Stuffed String is:" << stuffed << endl;
    return 0;
}