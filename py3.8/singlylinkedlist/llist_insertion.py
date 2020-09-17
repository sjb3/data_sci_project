'''
            array     list
--------------------------
insert/del  O(n)      O(1)
access el   O(1)      O(n)

contiguous   Y         N
memory

'''


class Node:  # represents el
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('No prev node to insert')
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        # if deleting node is head
        cur_node = self.head

        if cur_node and cur_node.head == key:
            self.head = cur_node.next
            cur_node = None
            return

        # 2 deleting node is not head
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def is_palindrome(self):
        # Method 1
        # s = ''
        # p = self.head
        # while p:
        #     s += p.data
        #     p = p.next

        # return s == s[::-1]

        # Method 2
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next

        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True


llist = LinkedList()
# llist.append('A')
# llist.append('B')
# llist.prepend(1)
# llist.prepend(234)
# # print(llist.head.next.data, '**')
# llist.delete_node('B')
# llist.print_list()

llist.append('R')
llist.append('0')
llist.append('0')

print(llist.is_palindrome())
