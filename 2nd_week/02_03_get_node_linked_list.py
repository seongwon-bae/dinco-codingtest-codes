class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        now = 0
        cur = self.head
        while now <= index:
            if now==index:
                print(f'{index}번째 노드는 {cur}이고 data는 {cur.data}입니다.')
                return cur
            now += 1
            cur = cur.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.get_node(1) # -> 5를 들고 있는 노드를 반환해야 합니다!