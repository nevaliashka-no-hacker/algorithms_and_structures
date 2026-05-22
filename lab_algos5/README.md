# Деревья

## Теория

### Проблема

> [!TIP]
> Подробнее проблемы описаны [в отдельном файле](real_problems.md).

В целом, почти любые задачи, в которых важны:
- Иерархия
- Быстрый поиск в упорядоченных данных
- Поиск по префиксу
- Работа с приоритетами
- Запросы на диапазонах
- Структурный разбор выражений или документов

### Решение

**Что такое дерево?**
Связная ациклическая структура данных.

```
           10          ← корень (root)
          /  \
         5    15       ← внутренние узлы
        / \     \
       3   7    20     ← листья (leaves) - у них нет потомков
```

**Типы деревьев:**
- Бинарное дерево
- Бинарное дерево поиска (BST)
- AVL-дерево
- Красно-черное дерево
- B-дерево

| Термин | Определение |
|--------|-------------|
| **Узел (node)** | Элемент дерева, хранит значение |
| **Корень (root)** | Самый верхний узел, не имеет родителя |
| **Лист (leaf)** | Узел без детей |
| **Высота (height)** | Длина самого длинного пути от корня до листа |
| **Глубина (depth)** | Расстояние от корня до данного узла |
| **Поддерево** | Любой узел + все его потомки |
| **BST (Binary Search Tree)** | Левый потомок < родитель < правый потомок |

**Ключевые свойства BST:**
- Поиск, вставка, удаление: **$O(h)$**, где $h$ - высота
- В сбалансированном дереве: $h = O(log n)$
- В вырожденном случае (списке): $h = O(n)$


| Операция | BST (средний) | BST (худший) | AVL/RB дерево |
|----------|---------------|--------------|---------------|
| Вставка  | $O(log n)$    | $O(n)$       | $O(log n)$    |
| Поиск    | $O(log n)$    | $O(n)$       | $O(log n)$    |
| Удаление | $O(log n)$    | $O(n)$       | $O(log n)$    |


## 2. Практика: Реализация двоичного дерева поиска

### Определение узла

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Вставка

```python
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

# Построение дерева из списка
values = [10, 5, 15, 3, 7, 20]
root = None
for v in values:
    root = insert(root, v)
```

### Поиск

```python
def search(root, val):
    if root is None or root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)

# Пример:
node = search(root, 7)
print(node.val if node else "Не найден")  # 7
```

### Нахождение минимума/максимума

```python
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
```

### Удаление узла

```python
def delete(root, val):
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
```

## 3. Обходы дерева

### Три вида DFS (глубина) - запоминаем по позиции "корня"

```python
def inorder(root):
    """Левый → Корень → Правый  (даёт отсортированный порядок в BST!)"""
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    """Корень → Левый → Правый  (копирование / сериализация дерева)"""
    if root is None:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    """Левый → Правый → Корень  (удаление дерева / вычисление выражений)"""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]

# Для нашего дерева [10, 5, 15, 3, 7, 20]:
print(inorder(root))    # [3, 5, 7, 10, 15, 20]  ← отсортировано!
print(preorder(root))   # [10, 5, 3, 7, 15, 20]
print(postorder(root))  # [3, 7, 5, 20, 15, 10]
```

### BFS (ширина) - обход по уровням

```python
from collections import deque

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

print(level_order(root))  # [[10], [5, 15], [3, 7, 20]]
```

### Визуальная шпаргалка по обходам

```
Пример для дерева [10, 5, 15, 3, 7, 20]:

           10
          /  \
         5    15
        / \     \
       3   7    20
```

- **Inorder**   (L-N-R): 3 → 5 → 7 → 10 → 15 → 20
- **Preorder**  (N-L-R): 10 → 5 → 3 → 7 → 15 → 20
- **Postorder** (L-R-N): 3 → 7 → 5 → 20 → 15 → 10
- **Level-order** (BFS): [10] → [5,15] → [3,7,20]

## 4. Применение в реальных задачах

### 4.1. Файловая система - дерево каталогов

```
/home
└── user
    ├── documents
    │   ├── report.pdf
    │   └── notes.txt
    └── photos
        └── vacation.jpg
```

```python
class FileNode:
    def __init__(self, name, is_dir=False):
        self.name = name
        self.is_dir = is_dir
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, indent=0):
    """Рекурсивный обход - аналог команды `tree` в терминале"""
    print("  " * indent + ("📁 " if node.is_dir else "📄 ") + node.name)
    for child in node.children:
        print_tree(child, indent + 1)

# Построение
root = FileNode("home", True)

user = FileNode("user", True)

docs = FileNode("documents", True)
docs.add_child(FileNode("report.pdf"))
docs.add_child(FileNode("notes.txt"))

photos = FileNode("photos", True)
photos.add_child(FileNode("vacation.jpg"))

user.add_child(docs)
user.add_child(photos)
root.add_child(user)

print_tree(root)
```

### 4.2. Автодополнение (Trie / префиксное дерево)

```python
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

    def autocomplete(self, prefix):
        """Возвращает все слова с данным префиксом"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, path, results):
        if node.is_end:
            results.append(path)
        for ch, child in node.children.items():
            self._dfs(child, path + ch, results)

# Пример: поисковые строки Yandex, DuckDuckGo, Google
trie = Trie()
for word in ["apple", "app", "application", "apt", "banana"]:
    trie.insert(word)

print(trie.autocomplete("app"))  # ['app', 'apple', 'application']
print(trie.autocomplete("b"))    # ['banana']
```

### 4.3. Другие реальные применения

| Структура | Где используется |
|-----------|-----------------|
| **BST / AVL / Red-Black** | `std::map`, `TreeMap`, индексы БД |
| **B-дерево / B+** | Индексы в PostgreSQL, MySQL, файловые системы (NTFS, ext4) |
| **Trie** | Автодополнение, спеллчекер, роутинг IP-адресов |
| **Heap (куча)** | Приоритетная очередь, алгоритм Дейкстры, `heapq` в Python |
| **Дерево отрезков** | Запросы на отрезках (сумма, минимум) за O(log n) |
| **AST** | Компиляторы и интерпретаторы (разбор выражений) |
| **DOM-дерево** | Браузеры - структура HTML-страницы |
| **Дерево решений** | Machine Learning (Random Forest, XGBoost, Minimax) |
