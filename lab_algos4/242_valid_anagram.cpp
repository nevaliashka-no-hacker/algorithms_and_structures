#include <iostream>
#include <string>
#include <unordered_map>

bool isAnagram(std::string s, std::string t) {
    if (s.size() != t.size()) {
        return false;
    }

    std::unordered_map<char, int> hash;
    for (int i = 0; i < s.size(); i++) {
        hash[s[i]] = i;
    }

    for (char c : s) {
        hash[c]++;
    }

    for (char c : t) {
        hash[c]--;
        if (hash[c] < 0) {
            return false;
        }
    }
    return true;
}

int main() {
    std::string s = "anagram";
    std::string t = "nagaram";
    std::cout << isAnagram(s, t);
    // добавить тесты
    return 0;
}