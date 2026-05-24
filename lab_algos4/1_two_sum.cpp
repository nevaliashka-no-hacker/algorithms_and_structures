#include <iostream>
#include <vector>
#include <unordered_map>

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

int main() {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> result = twoSum(nums, target);

    for (int i = 0; i < result.size(); i++) {
        std::cout << result[i] << ' ';
    }

    return 0;
}
