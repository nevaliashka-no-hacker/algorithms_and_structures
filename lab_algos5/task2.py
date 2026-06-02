"""
2. Написать все 4 типа обхода
"""

from collections import deque

class TreeNode:
    """Класс узла"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val):
    """Добавление узла"""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

#1
def inorder(root):
    """Левый → Корень → Правый  (даёт отсортированный порядок в BST!)"""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

#2
def preorder(root):
    """Корень → Левый → Правый  (копирование / сериализация дерева)"""
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

#3
def postorder(root):
    """Левый → Правый → Корень  (удаление дерева / вычисление выражений)"""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

#4
def level_order(root):
    """Обход по уровням - очередь"""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

def main():
    values = [10, 5, 15, 3, 7, 20]
    root = None
    for v in values:
        root = insert(root, v)

    print("1", inorder(root))
    print("2", preorder(root))
    print("3", postorder(root))
    print("4", level_order(root))

if __name__ == "__main__":
    main()