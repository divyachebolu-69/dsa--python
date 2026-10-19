
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


first = Node(20)
second = Node(30)
third = Node(40)


first.next = second
second.prev = first
second.next = third
third.prev = second


new_node = Node(10)
new_node.next = first
first.prev = new_node
first = new_node


temp = first
while temp:
    print(temp.data, end=" ")
    temp = temp.next
