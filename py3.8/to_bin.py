

def to_bin(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
            n = n//2
        else:
            n = n//2
    return count


print(to_bin(9))


def to_bin_recur(n):
    if n <= 0:
        return 0

    if n % 2 == 1:
        return 1 + to_bin_recur(n//2)
    else:
        return to_bin_recur(n//2)


print(to_bin_recur(9))
