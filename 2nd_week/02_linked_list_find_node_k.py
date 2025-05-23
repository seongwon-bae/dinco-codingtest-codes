class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.length = 1

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
        self.length += 1

    def get_kth_node_from_last(self, k):
        find_index = self.length - k
        count = 0
        cur = self.head
        while count<find_index:
            cur = cur.next
            count+=1
        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(3).data)  # 7이 나와야 합니다!