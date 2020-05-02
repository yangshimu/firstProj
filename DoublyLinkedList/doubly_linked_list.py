

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        cur = self.head
        while cur:
            print(cur.key)
            cur = cur.next

    def list_search(self, k):
        cur = self.head
        while cur is not None and cur.key != k:
            cur = cur.next
        return cur

    def list_insert(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        node.prev = None
        self.head = node

    def list_delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev


class DoublyLinkedListSentinel:
    def __init__(self):
        self.nil = Node()
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def list_search(self, key):
        cur = self.nil.next
        while cur is not None and cur.key != key:
            cur = cur.next
        return cur

    def list_insert(self, node):
        node.next = self.nil.next
        self.nil.next.prev = node
        self.nil.next = node
        node.prev = self.nil

    def list_delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def list_print(self):
        cur = self.nil.next
        while cur is not self.nil:
            print(cur.key)
            cur = cur.next


DL = Node(9)
head = DL

DL.next = Node(16)
DL.next.prev = DL
DL = DL.next
x = DL

L = DoublyLinkedList()
L.list_insert(Node(9))
L.list_insert(x)
L.list_insert(Node(4))
L.list_insert(Node(1))
L.list_print()

print(L.list_search(4).key)

L.list_insert(Node(500))
L.list_print()

L.list_delete(x)
L.list_print()

# L = DoublyLinkedListSentinel()
# L.list_insert(Node(9))
# L.list_insert(x)
# L.list_insert(Node(4))
# L.list_insert(Node(1))
# L.list_print()
#
# print(L.list_search(4).key)
#
# L.list_insert(Node(100))
# L.list_print()
#
# L.list_delete(x)
# L.list_print()

