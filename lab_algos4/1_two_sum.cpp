#include <iostream>
#include <vector>
#include <unordered_map>

#include "task1.hpp"

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> hash;
    for (int i = 0; i < nums.size(); i++) {
        hash[nums[i]] = i;
    }

    int temp;
    for (int i = 0; i < nums.size(); i++) {
        temp = target - nums[i];
        if (hash.find(temp) != hash.end() && hash[temp] != i) {
            return {i, hash[temp]};
        }
    }
    return {};
}