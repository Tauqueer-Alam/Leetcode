#include <sstream>
class Solution {
public:
    int lengthOfLastWord(string s) {
        vector<string> words;

        string word;
        stringstream ss(s);

        while (ss >> word) {
            words.push_back(word);
        }

        int last_index = words.size() - 1;
        string last_word = words[last_index];

        return last_word.size();
    }
};