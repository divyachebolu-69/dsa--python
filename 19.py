
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.prev = first

second.next = third
third.prev = second


temp = first
while temp:
    print(temp.data, end=" ")
    temp = temp.next
