class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
            self.bottom = new_node
        else:
            temp = self.top
            self.top = new_node
            new_node.next = temp
        self.length += 1

    def pop(self):
        if self.top == None:
            return None
        if self.top == self.bottom:
            self.bottom = None
        popped_element = self.top  # this way we can access popped element if we want
        self.top = self.top.next
        self.length -= 1


s = stack()
s.push(5)
s.push(100)
s.push(3)
s.push(11)
print(s.length)
print(s.peek())
s.pop()
print(s.peek())
s.pop()
print(s.peek())
print(s.length)