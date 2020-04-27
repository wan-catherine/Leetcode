# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        parent_node, deleted_node = self.query_key_parent_node(root, key)
        if not deleted_node:
            return root
        replace_node = self.find_replace_node(deleted_node)

        if parent_node:
            is_left = True if deleted_node == parent_node.left else False
            if is_left:
                parent_node.left = replace_node
            else:
                parent_node.right = replace_node

        if deleted_node == root:
            root = replace_node
        return root

    def find_replace_node(self, deleted_node):
        if not deleted_node.left and not deleted_node.right:
            return None
        if deleted_node.left and deleted_node.right:
            succssor = self.find_succssor(deleted_node)
            if succssor != deleted_node.right:
                # deleted_node.right.left = succssor.right
                succssor.right = deleted_node.right
                # deleted_node.right = succssor
            succssor.left = deleted_node.left
            return succssor
        elif deleted_node.left:
            return deleted_node.left
        else:
            return deleted_node.right

    def find_succssor(self, deleted_node):
        current = deleted_node.right
        while current and current.left:
            current = current.left
        return current

    def query_key_parent_node(self, root, key):
        if root.val == key:
            return None, root
        parent_node = root
        if root.val < key:
            current = root.right
        else:
            current = root.left
        while current:
            if current.val == key:
                return parent_node, current
            parent_node = current
            if current.val < key:
                current = current.right
            else:
                current = current.left
        return parent_node, current


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            line = next(lines)
            key = int(line);

            ret = Solution().deleteNode(root, key)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()