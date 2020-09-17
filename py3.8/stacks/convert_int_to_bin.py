from stack_reverse import Stack


def div_by_2(num):
    s = Stack()

    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num = num // 2

    bi_num = ''

    while not s.is_empty():
        bi_num += str(s.pop())

    return bi_num


print(div_by_2(242))
