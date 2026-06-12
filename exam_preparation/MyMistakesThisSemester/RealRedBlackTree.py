

rbt = RedBlackTree()
for v in [7, 3, 18, 10, 22, 8, 11, 26]:
    rbt.insert(v)
print("RB Tree inorder:", rbt.inorder())  # [3, 7, 8, 10, 11, 18, 22, 26]