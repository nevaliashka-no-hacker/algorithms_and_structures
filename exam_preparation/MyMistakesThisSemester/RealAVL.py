class TreeNode:
    def __init__(self, key):
        self.root = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_height(y)
        self._update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update_height(x)
        self._update_height(y)
        return y

    

avl = AVLTree()
for v in [10, 20, 30, 40, 50, 25]:
    avl.insert(v)
print("AVL inorder:", avl.inorder())  # [10, 20, 25, 30, 40, 50]
print("AVL root:", avl.root.key)  # 30 