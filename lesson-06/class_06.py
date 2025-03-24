import dataclasses
from typing import Any, Optional


@dataclasses.dataclass
class Node:
    val: Any
    nxt: Optional["Node"]


# remove_node(head, k)
# 1 -> 2 -> 5 -> 3: del 5
# 1 -> 2 -> 3

# 1 -> 2 -> 5 -> 3: del 1
# 2 -> 5 -> 3


def del_node(head, k):
    if not head:
        return head
    if head.val==k:
        return head.nxt
    cur = head
    while cur.nxt:
        if cur.nxt.val == k:
            cur.nxt = cur.nxt.nxt
            return head
        cur=cur.nxt
    return head


#cell.list_head = del_node(cell.list_head, k)


# 1 -> 2 -> 5 -> 3
# 3 -> 5 -> 2 -> 1


def reverse_list(head: Optional[Node]) -> Optional[Node]:
    curr = head
    prev = None

    while curr:
        next_node = curr.nxt

        curr.nxt = prev

        prev = curr
        curr = next_node

    return prev




class Bad:
    def __hash__(self):
        return 100


b1 = Bad()
b2 = Bad()
b3 = Bad()

dct = {}
dct[b1] = 1  # O(n)
dct[b2] = 2  # O(n)
dct[b3] = 3  # O(n)



print(hash(b1), hash(b2), hash(b3))

# [1, 2, 5, 3], k == 4 -> (0, 3)
# [1, 2, 5, 2], k == 4 -> (1, 3)
# [1, 2, 5, 3], k == 10 -> None

def find_sum_k(nums: list[int], k: int) -> Optional[tuple[int, int]]:
    diff = dict()
    for i in range(len(nums)):
        if k-nums[i] in diff:
            return (diff[k-nums[i]], i)
        else:
            diff[nums[i]] = i
    return None


assert find_sum_k([1, 2, 5, 3], 4) == (0, 3)
assert find_sum_k([1, 2, 5, 2], 4) == (1, 3)
assert find_sum_k([1, 2], 3) == (0, 1)
assert find_sum_k([1, 2, 5, 9], 4) is None
assert find_sum_k([1], 4) is None
assert find_sum_k([], 4) is None


print("ok")
