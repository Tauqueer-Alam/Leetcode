#include <algorithm>
#include <string>
#include <climits>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        bool negative = false;

        if (x < 0) {
            negative = true;
        }

        string str = to_string(x);

        // Remove '-' before reversing
        if (negative) {
            str = str.substr(1);
        }

        std::reverse(str.begin(), str.end());

        long long result = stoll(str);

        if (negative) {
            result = -result;
        }

        // Check 32-bit integer range
        if (result > INT_MAX || result < INT_MIN) {
            return 0;
        }

        return (int)result;
    }
};