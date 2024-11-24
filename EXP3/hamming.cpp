#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> data(5), hamming(9);
    cout << "Enter the 5 data bits (0 or 1):" << endl;
    for (int i = 0; i < 5; i++) cin >> data[i];

    hamming = {0, 0, data[0], 0, data[1], data[2], data[3], 0, data[4]};

    hamming[0] = hamming[2] ^ hamming[4] ^ hamming[6] ^ hamming[8];
    hamming[1] = hamming[2] ^ hamming[5] ^ hamming[6];
    hamming[3] = hamming[4] ^ hamming[5] ^ hamming[6];
    hamming[7] = hamming[8];

    cout << "Hamming code: ";
    for (int i = 8; i >= 0; i--) cout << hamming[i] << " ";
    cout << endl;

    return 0;
}


//python
// data = input("Enter Data: ")

// d = [int(x) for x in data]
// p1 = d[0] ^ d[1] ^ d[3] ^ d[4]
// p2 = d[0] ^ d[2] ^ d[3]
// p4 = d[1] ^ d[2] ^ d[3]
// p8 = d[4]
// hamming = [p1, p2, d[0], p4, d[1], d[2], d[3], p8, d[4]]

// print(f"Hamming Code: {''.join(map(str, reversed(hamming)))}")