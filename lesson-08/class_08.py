from collections import deque


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# [0, 1, 2, 3, 4, 5]


def list_to_BST(array):
    begin_idx = 0
    end_idx = len(array)-1

    deque_object = deque([(begin_idx, end_idx, None)])
    root = None
    while deque_object:
        cur_begin, cur_end, parent = deque_object.popleft()
        if cur_end < cur_begin:
            continue
        cur_center = (cur_end+cur_begin)//2
        new_node = Node(array[cur_center])
        if parent:
            if parent.key < new_node.key:
                parent.right = new_node
            else:
                parent.left = new_node
        else:
            root = new_node
        deque_object.extend(
            [
                (cur_begin,cur_center-1, new_node),
                (cur_center+1, cur_end, new_node)
            ]
        )
    return root


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.key))
        if node.left or node.right:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

arr = [1, 2, 3, 4, 5]
bst = list_to_BST(arr)

print_tree(bst)
