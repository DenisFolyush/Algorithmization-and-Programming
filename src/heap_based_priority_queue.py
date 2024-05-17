class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def get(self, i):
        return self.items[i]

    def get_max(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def extract_max(self):
        if self.size() == 0:
            return None
        max_element = self.get_max()
        if self.size() == 1:
            del self.items[0::]
            return max_element.value
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return max_element.value

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        highest = i

        if l < self.size() and self.get(l).priority > self.get(highest).priority:
            highest = l
        if r < self.size() and self.get(r).priority > self.get(highest).priority:
            highest = r

        if highest != i:
            self.swap(highest, i)
            self.max_heapify(highest)

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert(self, value, priority):
        node = Node(value, priority)
        index = self.size()
        self.items.append(node)

        while index != 0:
            p = self.parent(index)
            if self.get(p).priority < self.get(index).priority:
                self.swap(p, index)
            elif self.get(p).priority == self.get(index).priority and self.get(p).value < self.get(index).value:
                self.swap(p, index)
            else:
                break
            index = p

    def peek(self):
        if self.size() == 0:
            return None
        return self.items[0].value

    def __str__(self):
        return ', '.join(str(node.value) for node in self.items)
