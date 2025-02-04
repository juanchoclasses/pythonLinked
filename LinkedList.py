
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def map(self, func):
        current = self.head
        new_ll = LinkedList()

        while current:
            new_ll.insert(func(current.data))
            current = current.next

        return new_ll

    def filter(self, func):
        current = self.head
        new_ll = LinkedList()

        while current:
            if func(current.data):
                new_ll.insert(current.data)
            current = current.next

        return new_ll

    def reduce(self, func, initial):
        current = self.head
        result = initial

        while current:
            result = func(result, current.data)
            current = current.next

        return result

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(10)
    ll.insert(30)
    ll.insert(20)

    ll.insert(40)
    ll.insert(50)
    ll.display()
    ll.reverse()
    ll.display()
    ll.delete(30)
    ll.display()
    ll.delete(10)
    ll.display()
    ll.delete(50)
    ll.display()
    ll.delete(60)
    ll.display()
    ll.delete(40)
    ll.display()

    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(40)
    ll.insert(50)

    ll.map(lambda x: x * 2).display()
    ll.filter(lambda x: x % 4 == 0).display()
    print(ll.reduce(lambda x, y: x + y, 0))