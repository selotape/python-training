from collections import OrderedDict
from copy import deepcopy
from math import sqrt, floor


# explicitly explain assumptions (python3 XXX - float division)
# discuss typing. add comments about assumptions and TODOs
# show =craftmanship!=
# no magic numbers!
# discuss extreme inputs. LEARN extreme inputs
# learn arithmetics
# don't smart-ass

# each day: LEARN BY HEART 10 algos

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.other = None


def deep_copy_list(head: Node) -> Node:
    current = head
    nodes_mapping = OrderedDict()
    while current is not None:
        current_copy = get_copy_or_create(current, nodes_mapping)
        current_copy.next = get_copy_or_create(current.next, nodes_mapping)
        current_copy.other = get_copy_or_create(current.other, nodes_mapping)
        current = current.next

    return next(nodes_mapping.values())


def get_copy_or_create(node, mapping):
    if node is None:
        return None

    if node in mapping:
        return mapping[node]

    node_copy = Node(deepcopy(node.value))
    mapping[node] = node_copy
    return node_copy



if __name__ == '__main__':
    head = Node()

def values(node):
    while node is not None:
        yield node.value
        node = node.next

def nodes(node):
    while node is not None:
        yield node
        node = node.next

def assert_lists_equal_but_different(head1, head2):
    assert values(head1) == values(head2)
    nodes1, nodes2 = nodes(head1), nodes(head2)
    assert len(nodes1) == len(nodes2)

def normalize(head: Node) -> Generator[Tuple[int, object, object]]:
    ptr = head
    while ptr != None:
        yield ptr

def foo1(ptr):
    return (ptr.value, ptr.other.value if ptr.other else None, ptr.next.value if ptr.next else None)

def foo2(ptr):
    return ptr


    # assert str(sqrt_(200))[:6] == str(sqrt(200))[:6], 'fail'
    # assert str(sqrt_(789))[:6] == str(sqrt(789))[:6], 'fail'


def sqrt_(num: int):
    scaled_num = num * 1000000
    int_sqrt_num = int_sqrt(scaled_num)
    return int_sqrt_num / 1000


def int_sqrt(num):
    return int(floor(sqrt(num)))

