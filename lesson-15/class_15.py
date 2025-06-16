# LRU cache

class LRUCache:
    def __init__(self, n):
        self.data = {}
        self.capacity = n
        if self.capacity <= 0:
            raise Exception('Некорректное значение n')
    
    def get(self, key):
        if key not in self.data:
            return None
        
        value = self.data.pop(key)
        self.data[key] = value
        return value
    
    def set(self, key, value):
        if key in self.data:
            self.data.pop(key)
            self.data[key] = value
        else:
            if len(self.data) >= self.capacity:
                self.data.pop(next(iter(self.data)))
                
            self.data[key] = value
        

lru = LRUCache(2)

lru.set(1, 11)
lru.set(2, 22)
lru.set(3, 33)

assert lru.get(1) is None
assert lru.get(2) == 22
assert lru.get(3) == 33


lru = LRUCache(2)

lru.set(1, 11)
lru.set(2, 22)
assert lru.get(2) == 22
assert lru.get(1) == 11

lru.set(3, 33)

assert lru.get(1) == 11
assert lru.get(2) is None
assert lru.get(3) == 33
print("lru - ok")






#      5
#  3      9
#1   4  7   11

# 1 -> 3 -> 4 -> 5 -> 7 -> 9 -> 11


class TreeNode:
    val: Any
    left: TreeNode
    right: TreeNode


class ListNode:
    val: Any
    next: ListNode


def treeToList(root: TreeNode) -> ListNode:
    sorted_list = None
    first_node = None
    tree_node = root
    list_nodes = []

    while tree_node is not None or list_nodes:
        while tree_node is not None:
            list_nodes.append(tree_node)
            tree_node = tree_node.left
        
        tree_node = list_nodes.pop()

        if sorted_list:
            sorted_list.next = ListNode(tree_node.val, None)
            sorted_list = sorted_list.next
        else:
            first_node = sorted_list = ListNode(tree_node.val, None)
        
        tree_node = tree_node.right
        
    return first_node
        
        
   
    






