#include "task1.hpp"

#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
    std::cout << "Two sum" << std::endl;
    std::vector<int> nums1 = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> result1 = twoSum(nums1, target);
    for (int i = 0; i < result1.size(); i++) {
        std::cout << result1[i] << ' ';
    }
    std::cout << std::endl;

    std::cout << "\nValidAnagram" << std::endl;
    std::string s = "anagram";
    std::string t = "nagaram";
    std::cout << isAnagram(s, t) << std::endl;

    std::cout << "\nRansomNote" << std::endl;
    std::string ransomNote = "aa";
    std::string magazine = "aab";
    std::cout << canConstruct(ransomNote, magazine) << std::endl;

    std::cout << "\nTopKFrequenceElement" << std::endl;
    int k = 2;
    std::vector<int> nums347 = {1, 1, 1, 2, 2, 3};
    std::vector<int> result347 = topKFrequent(nums347, k);
    for (int i = 0; i < result347.size(); i++) {
        std::cout << result347[i] << ' ';
    }
    std::cout << std::endl;

    std::cout << "\nFirstMissingPositive" << std::endl;
    std::vector<int> nums41 = {3, 4, -1, 1};
    std::cout << firstMissingPositive(nums41) << std::endl;

    return 0;
}