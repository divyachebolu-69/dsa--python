class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(50)
head.next.next = Node(5)

minimum = head.data
temp = head.next

while temp:
    if temp.data < minimum:
        minimum = temp.data
    temp = temp.next

print("Minimum:", minimum)