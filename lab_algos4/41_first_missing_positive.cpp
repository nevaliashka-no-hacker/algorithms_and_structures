#include <iostream>
#include <vector>
#include <unordered_map>

#include "task1.hpp"

using namespace std;

int firstMissingPositive(vector<int>& nums) {
    unordered_map<int, int> hash;
    for (int i = 0; i < nums.size(); i++) {
        hash[nums[i]] = i;
    }

    int res = 1;
    while(1) {
        if (hash.find(res) != hash.end()) {
            res++;
        }
        else {
            return res;
        }
    }

    return 0;
}
