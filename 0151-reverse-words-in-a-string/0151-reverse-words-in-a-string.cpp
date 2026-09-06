class Solution {
public:
    string reverseWords(string s) {
        // Remove leading and trailing spaces
        s.erase(0, s.find_first_not_of(' '));
        s.erase(s.find_last_not_of(' ') + 1);

        // Split words
        stringstream ss(s);
        vector<string> words;
        string word;

        while (ss >> word) {
            words.push_back(word);
        }

        // Reverse words
        reverse(words.begin(), words.end());

        // Join words
        string result;
        for (int i = 0; i < words.size(); i++) {
            if (i > 0) result += " ";
            result += words[i];
        }

        return result;
    }
};