#include <iostream>
#include <unordered_map>

#include "task1.hpp"

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
