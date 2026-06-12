from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def insert(self, key):
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return None
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        
        return node
    
    def _min_node(self, node):
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur
    
    def inorder(self):
        return self._inorder(self.root)
    
    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.key] + self._inorder(node.right)
    
    def preorder(self):
        return self._preorder(self.root)
    
    def _preorder(self, node):
        if node is None:
            return []
        return [node.key] + self._preorder(node.left) + self._preorder(node.right)
    
    def postorder(self):
        return self._postorder(self.root)
    
    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.key]
    
    def level_order(self):
        if self.root is None:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.key)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

values = [10, 5, 15, 3, 7, 20]
bst = BinarySearchTree()
for v in values:
    bst.insert(v)

node = bst.search(7)
print(node.key if node else "Not found")  # 7

print(bst.inorder())    # [3, 5, 7, 10, 15, 20]
print(bst.preorder())   # [10, 5, 3, 7, 15, 20]
print(bst.postorder())  # [3, 7, 5, 20, 15, 10]
print(bst.level_order()) # [[10], [5, 15], [3, 7, 20]]
