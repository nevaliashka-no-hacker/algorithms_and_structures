#include <iostream>
#include <vector>
#include <unordered_map>

#include "task1.hpp"

using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    int n = nums.size();

    unordered_map<int, int> hash;

    // подсчет элементов
    for (int num : nums) {
        hash[num]++;
    }

    // пихаеи по корзинкам
    vector<vector<int>> buckets(nums.size() + 1);
    for (auto& pair : hash) {
        int num = pair.first;
        int count = pair.second;
        buckets[count].push_back(num);
    }

    vector<int> result;
    int temp = 0;
    for (int i = n; i >= 0; i--) {
        for (int j = 0; j < buckets[i].size(); j++) {
            result.push_back(buckets[i][j]);
            temp++;
            if (temp == k) {
                return result;
            }
        }
        if (temp == k) {
            return result;
        }
    }
        
    return result;
}

