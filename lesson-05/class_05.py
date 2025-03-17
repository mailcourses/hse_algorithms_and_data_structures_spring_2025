class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


n1 = TreeNode(1)
n4 = TreeNode(4)
n3 = TreeNode(3, left=n1, right=n4)
n6 = TreeNode(6)
n7 = TreeNode(7, left=n6)
root = TreeNode(5, left=n3, right=n7)

#      5
#  3      7
#1   4   6

# bfs_level = [[5], [3, 7], [1, 4, 6]]

#Используется очередь, в которой хранятся вершины, требующие просмотра.
# За одну итерацию алгоритма:
#● если очередь не пуста, извлекается вершина из очереди,
#● посещается (обрабатывается) извлеченная вершина,
#● в очередь помещаются все дочерние.

from collections import deque


def level_bfs(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []

    bfs_level = []
    queue = deque([root])

    while queue:
        level = []
        size = len(queue)

        for i in range(size):
            root = queue.popleft()
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

            level.append(root.val)
        bfs_level.append(level)

    return bfs_level


assert level_bfs(root) == [[5], [3, 7], [1, 4, 6]]
assert level_bfs(n7) == [[7], [6]]
assert level_bfs(n6) == [[6]]
assert level_bfs(None) == []


###############

def find_dfs(root: TreeNode | None, k: int) -> TreeNode | None:
    if not root:
        return None
    if root.val == k:
        return root

    return find_dfs(root.left, k) or find_dfs(root.right, k)


assert find_dfs(root, 5) is root
assert find_dfs(root, 3) is n3
assert find_dfs(root, 6) is n6
assert find_dfs(root, 2) is None
assert find_dfs(root, 10) is None
assert find_dfs(None, 3) is None



#      5
#  3      7
#1   4   6



def is_bst(
    root: TreeNode | None,
    leq: float = float('-inf'),
    geq: float = float('inf'),
) -> bool:
    if not root:
        return True

    if not (root.val > leq and root.val < geq):
        return False

    left = is_bst(root.left, geq=root.val, leq=leq)
    right = is_bst(root.right, leq=root.val, geq=geq)

    return left and right


assert is_bst(root)
assert is_bst(n3)
assert is_bst(n4)
assert is_bst(n7)
assert is_bst(n6)
assert is_bst(n1)
assert is_bst(None)


#      5
#  3      7
#1   6   6

no1 = TreeNode(1)
no4 = TreeNode(6)
no3 = TreeNode(3, left=no1, right=no4)
no6 = TreeNode(6)
no7 = TreeNode(7, left=no6)
root_no = TreeNode(5, left=no3, right=no7)

assert not is_bst(root_no)
assert is_bst(no3)


print("ok")
