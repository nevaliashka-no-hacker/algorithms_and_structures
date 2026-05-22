# Лабораторная работа 5: Деревья

> **Главный паттерн:** большинство задач на деревья решаются через **рекурсию**, где вы:
> 1. Обрабатываете базовый случай (`if root is None`)
> 2. Рекурсивно решаете для `root.left` и `root.right`
> 3. Комбинируете результаты

## Практика
1. Реализовать BST с:
   - вставкой
   - поиском
   - удалением
2. Написать все 4 типа обхода
3. Решить 5 или более задач с LeetCode (из них минимум 2 medium/hard)

## Задачи на LeetCode

### Базовый уровень

| # | Задача | Ключевая идея |
|---|--------|---------------|
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Рекурсия / BFS |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Рекурсивный swap |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Параллельный обход |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Зеркальное сравнение |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Inorder - стек/рекурсия |
| 543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Высота левого + правого |
| 110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Проверка высот |
| 572 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Рекурсия + Same Tree |
| 700 | [Search in a BST](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Базовый поиск в BST |
| 108 | [Convert Sorted Array to BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Бинарное деление |

### Средний уровень

| # | Задача | Ключевая идея |
|---|--------|---------------|
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS по уровням |
| 98 | [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) | Диапазон (lo, hi) |
| 230 | [Kth Smallest Element in BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Inorder + счётчик |
| 105 | [Construct BT from Preorder & Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Рекурсивное построение |
| 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | BFS, последний на уровне |
| 236 | [Lowest Common Ancestor](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | LCA - рекурсия |
| 208 | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Префиксное дерево |
| 450 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | 3 случая удаления |
| 114 | [Flatten BT to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Preorder → список |
| 1448 | [Count Good Nodes in BT](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | DFS + текущий max |

### Продвинутый уровень

| # | Задача | Ключевая идея |
|---|--------|---------------|
| 124 | [Binary Tree Max Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | DFS + глобальный max |
| 297 | [Serialize & Deserialize BT](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Preorder + очередь |
| 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Trie + Backtracking |
