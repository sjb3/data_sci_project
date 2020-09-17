# Not using str()

def int_2_str(n):
    if n < 0:
        is_negative = True
        n *= -1
    else:
        is_negative = False

    output = []

    while n > 0:
        output.append(chr(ord('0')+(n % 10)))
        n = n // 10

    if is_negative:
        ans = ''.join([i for i in output[::-1]])
        print(type(ans))
        return '-' + ans

    ans = ''.join([i for i in output[::-1]])
    print(type(ans))
    return ans


print(int_2_str(-345))
