class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


node = Node(5)
print(node.data, node.next)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # 가장 끝 노드에 새 노드를 연결
    # value : 추가할 노드의 값
    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    # linked_list에서 저장한 head를 따라가면서 현재 노드를 전부 출력하는 함수
    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

linked_list = LinkedList(5)
print(linked_list.head.data)
linked_list.append(12)
linked_list.append(8)
print('print 시작')
linked_list.print_all()