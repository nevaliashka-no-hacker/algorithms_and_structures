#include <iostream>
#include <vector>
#include <string>

enum Status {
    FREE,
    BUSY,
    DELETED
};

struct HashNode {
    std::string key;
    int value;
    Status status;

    HashNode() : key(""), value(0), status(Status::FREE) {}
};

class HashTableOpenAddressing {
private:
    std::vector<HashNode> table;
    int capacity;
    int busy;

    int hash(std::string& key) {
        int hash = 0;
        for (char c : key) {
            hash = hash * 31 + c;
        }
        return hash;
    }

    int findIndex(std::string& key, bool& isFound) {
        int hashVal = hash(key);
        int start = hashVal % capacity;
        int foundDel = false;
        int firstDel = 0;
        int i = 0;
        
        while (i < capacity) {
            int cur = (start + i) % capacity;
            HashNode& node = table[cur];
            
            if (node.status == Status::FREE) {
                if (foundDel) {
                    isFound = false;
                    return firstDel;
                }
                isFound = false;
                return cur;
            }
            
            if (node.status == Status::DELETED && foundDel == false) {
                firstDel = cur;
            }
            
            if (node.status == Status::BUSY && node.key == key) {
                isFound = true;
                return cur;
            }
            
            ++i;
        }
        
        if (foundDel == true) {
            isFound = false;
            return firstDel;
        }
        
        isFound = false;
        return foundDel;
    }

    void rehash() {
        int oldCapacity = capacity;
        std::vector<HashNode> oldTable = std::move(table);
        
        capacity *= 2;
        table.clear();
        table.resize(capacity);
        
        size = 0;
        for (int i = 0; i < oldCapacity; ++i) {
            if (oldTable[i].status == Status::BUSY) {
                insert(oldTable[i].key, oldTable[i].value);
            }
        }
    }

public:
    void insert(const std::string& key, int value) {
        bool isFound = false;
        int index = findIndex(key, isFound);
        
        if (index == SIZE_MAX) {
            std::cout << "Hash table full" << std::endl;
            rehash();
        }
        if (isFound) {
            table[index].value = value;
        } 
        else {
            table[index].key = key;
            table[index].value = value;
            table[index].status = Status::BUSY;
            size++;
        }
    }

    void get(std::string& key, int& result) {
        bool isFound = false;
        int index = findIndex(key, isFound);
        
        if !(index == SIZE_MAX || !isFound) {
            std::cout << "Not value" << std::endl;
        }
        else {
            result = table[index].value;
        }
    }

    void remove(const std::string& key) {
        bool isFound = false;
        int index = findIndex(key, isFound);
        
        if ((!index == SIZE_MAX || !isFound)) {
            table[index].status = Status::DELETED;
            table[index].key = "";
            size--;
        }
    }

    bool search(const std::string& key) {
        bool isFound = false;
        findIndex(key, isFound);
        return isFound;
    }

    int getSize() {
        return size;
    }
};