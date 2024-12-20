#include <iostream>
#include <string>
using namespace std;

// Function to perform XOR operation
string xor_func(string a, string b) {
    string result = "";
    for (int i = 1; i < b.length(); i++) {
        result += (a[i] == b[i]) ? '0' : '1';
    }
    return result;
}

// Function to perform modulo-2 division
string mod2div(string dividend, string divisor) {
    int pick = divisor.length();
    string tmp = dividend.substr(0, pick);
    
    for (int i = pick; i <= dividend.length(); i++) {
        if (tmp[0] == '1') {
            tmp = xor_func(divisor, tmp) + dividend[i];
        }
        else {
            string zeros(pick, '0');
            tmp = xor_func(zeros, tmp) + dividend[i];
        }
    }

    return tmp;
}

int main() {
    string data = "1101011011";
    string key = "10011";
    
    int l_key = key.length();
    string appended_data = data;
    
    // Append zeros to data
    for (int i = 0; i < l_key - 1; i++) {
        appended_data += '0';
    }
    
    string remainder = mod2div(appended_data, key);
    string codeword = data + remainder;
    cout << "Encoded data: " << codeword << endl;
    
    return 0;
}