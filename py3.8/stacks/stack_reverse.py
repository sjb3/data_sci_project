# Basic Stack class and methods

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
      # return the top popped element
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


input = 'hello'
# print(input[::-1])
# print(list(i for i in reversed(input)))

stack = Stack()


def reverse_str(stack, input):
    # Loop through the string using push for each el
    for i in range(len(input)):
        stack.push(input[i])

    rev = ''
    while not stack.is_empty():
        rev += stack.pop()

    return rev


print(reverse_str(stack, input))
