class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, next):
        newNode = Node(data)
        if not head:
            return newNode

        current = head
        while current.next:
            current = current.next

        current.next = newNode
        return head
