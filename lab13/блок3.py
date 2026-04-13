import sys

# Узел дерева
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 1. Рекурсивный DFS
def dfs_recursive(node):
    if node is None:
        return
    # Логика обработки узла
    print(node.value, end=" ")
    dfs_recursive(node.left)
    dfs_recursive(node.right)

# 2. Итеративный DFS (через явный стек)
def dfs_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        # Сначала кладем правый, потом левый, 
        # чтобы левый обработался первым (принцип LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)