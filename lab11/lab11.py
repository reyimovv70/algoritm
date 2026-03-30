class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return BinaryTreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def search(root, value):
    if root is None:
        return None
    if root.value == value:
        return root

    if value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        min_node = min_value_node(root.right)
        root.value = min_node.value
        root.right = delete(root.right, min_node.value)

    return root


root = None

for num in [50, 30, 70, 20, 40, 60]:
    root = insert(root, num)

result = search(root, 40)

if result:
    print("Найден:", result.value)
else:
    print("Не найден")

root = delete(root, 30)

check = search(root, 30)

if check:
    print("Ошибка, не удалился")
else:
    print("Удаление прошло успешно")
print(search(root, 30).value)