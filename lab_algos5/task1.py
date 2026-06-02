"""
1. Реализовать BST с:
   - вставкой
   - поиском
   - удалением
"""

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

def search(root, val):
    """Поиск узла"""
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)

def find_min(root):
    """Минимум - самый левый узел"""
    current = root
    while current.left:
        current = current.left
    return current

def find_max(root):
    """Максимум - самый правый узел"""
    current = root
    while current.right:
        current = current.right
    return current

def delete(root, val):
    """Удаление узла"""
    if root is None:
        return None

    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # Случай 1: лист или один ребёнок
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # Случай 2: два ребёнка → заменяем на min из правого поддерева
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete(root.right, successor.val)

    return root

def main():
    values = [10, 5, 15, 3, 7, 20]
    root = None
    for v in values:
        root = insert(root, v)

    node = search(root, 7)
    print(node.val if node else "Не найден")

    afterdelete = delete(root, 7)
    node = search(afterdelete, 7)
    print(node.val if node else "Не найден")

if __name__ == "__main__":
    main()