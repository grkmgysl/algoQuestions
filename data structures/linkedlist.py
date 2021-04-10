class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def printl(self):
        counter = self.head
        arr = []
        while counter != None:
            arr.append(counter.data)
            counter = counter.next
        return print(arr)

    def insert(self, index, data):
        new_node = Node(data)
        if index == 1:
            self.prepend(data)
        else:
            i = 1
            counter = self.head
            while i < index - 1 and counter != None:
                counter = counter.next
                i += 1
            temp = counter.next
            counter.next = new_node
            new_node.next = temp
            self.length += 1

    def traversal(self, index):
        counter = self.head
        i = 1
        while counter != None and i < index:
            counter = counter.next
            i += 1
        return counter

    def remove(self, index):
        if index == 1:
            self.head = self.head.next
            self.length -= 1
        else:
            counter = self.traversal(index - 1)
            temp = counter.next
            counter.next = temp.next
            self.length -= 1


l = LinkedList()
l.append(10)
l.append(40)
l.append(5)
l.append(8)
l.append(1020)
# l.insert(3, 7)
l.remove(1)
l.printl()
