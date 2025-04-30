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
    def to_string_all(self):
        cur = self.head
        full_string_num = ''
        while cur.next != None:
            full_string_num += f'{cur.data}'
            cur = cur.next
        full_string_num += f'{cur.data}'
        return full_string_num


def get_linked_list_sum(linked_list_1, linked_list_2):
    linked_list_1_num = int(linked_list_1.to_string_all())
    linked_list_2_num = int(linked_list_2.to_string_all())
    return linked_list_1_num + linked_list_2_num


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))