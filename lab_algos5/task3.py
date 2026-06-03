"""
5 задач с LeetCode
"""

from collections import deque

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inTree(values):
    if not values or values[0] is None:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Левый ребенок
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Правый ребенок
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

def treeToList(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    while result and result[-1] is None:
        result.pop()
    
    return result

#100. Same Tree
def isSameTree(p, q):
    if p is None and q is None:
        return True
            
    if p is None or q is None:
        return False

    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False

#104. Maximum Depth of Binary Tree
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

#226. Invert Binary Tree
def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

#102. Binary Tree Level Order Traversal
def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

#98. Validate Binary Search Tree
def isValidBST(root):
    return validate(root, float('-inf'), float('inf'))

def validate(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

#208. Implement Trie (Prefix Tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
    
#297. Serialize and Deserialize Binary Tree
class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        vals = []
        dfs(root)
        return ",".join(vals)
    
    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        vals = iter(data.split(","))
        return dfs()

def main():
    print("Пример 100. Same Tree")
    a1 = [1, 2, 3]
    b1 = [1, 2, 3]
    atree1, btree1 = inTree(a1), inTree(b1)
    print(a1, "и", b1, ":", isSameTree(atree1, btree1))

    print()

    print("Пример 104. Maximum Depth of Binary Tree")
    root = [3, 9, 20, None, None, 15, 7]
    rootTree = inTree(root)
    print(root, ":", maxDepth(rootTree))

    print()

    print("Пример 226. Invert Binary Tree")
    root = [2,1,3]
    rootTree = inTree(root)
    result = treeToList(invertTree(rootTree))
    print(root, ":", result)

    print()

    print("Пример 98. Validate Binary Search Tree")
    root = [2,1,3]
    rootTree = inTree(root)
    print(root, ":", isValidBST(rootTree))

if __name__ == "__main__":
    main()
