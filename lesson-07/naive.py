from collections import deque

#          .
#        / | \
#       a  d  z
#      /
#     b

class SuffixTreeNode:
    def __init__(self, num):
        self.childs = {}
        self.num = num

class SuffixTree:
    def __init__(self, s: str):
        s += '$'
        self.root = SuffixTreeNode(-1)
        self.__build_tree(s)

    def __build_tree(self, s: str):
        for i in range(len(s)):
            suffix = s[i:]
            self.__add_suffix(suffix, i)

    def __add_suffix(self, suffix: str, idx: int):
        node = self.root
        n = len(suffix)
        for i in range(n):
            ch = suffix[i]
            if ch not in node.childs:
                node.childs[ch] = SuffixTreeNode(idx if i == n-1 else -1)
            node = node.childs[ch]

    def search(self, p: str) -> [int]:
        node = self.root
        results = []

        for ch in p:
            if ch in node.childs:
                node = node.childs[ch]
            else:
                return []

        queue = deque([node])
        while queue:
            node = queue.popleft()
            # Мы в листе
            if node.num != -1:
                results.append(node.num)
            for child in node.childs:
                queue.append(node.childs[child])
        return sorted(results)

if __name__ == "__main__":
    s = "xabxac"
    p = "xa"

    tree = SuffixTree(s)
    print(tree.search(p))

    s = "aaaaaa"
    p = "a"

    tree = SuffixTree(s)
    print(tree.search(p))

