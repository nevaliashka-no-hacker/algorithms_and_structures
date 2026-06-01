#include <iostream>
#include <unordered_map>

#include "task1.hpp"

using namespace std;

bool canConstruct(string ransomNote, string magazine) {
    unordered_map<int, char> hash;
    for (char simvol : magazine) {
           hash[simvol]++;
    }

    for (char simvol : ransomNote) {
        if (hash.find(simvol) != hash.end() && hash[simvol] > 0) {
            hash[simvol]--;
        }
        else {
            return false;
        }
    }
    return true;
}
