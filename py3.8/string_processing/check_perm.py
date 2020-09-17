is_perm_1 = 'dog'
is_perm_2 = 'god'

not_perm_1 = 'not'
not_perm_2 = 'top'

# time complexity = O(n)
# space complexity = O(n)


def is_permmutation(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    # sorted way time complexity = O(n log n)

    ht = dict()

    for s in str_1:
        if s in ht:
            ht[s] += 1
        else:
            ht[s] = 1

    for s in str_2:
        if s in ht:
            ht[s] -= 1
        else:
            ht[s] = 1

    for i in ht:
        if ht[i] != 0:
            return False
    # print(value == 0 for value in ht.values())
    # print(all(value == 0 for value in ht.values()))
    # print(ht.keys(), ht.values())
    # for k, v in ht.items():
    #     print(k, v)
    return True


print(is_permmutation('dOG', 'god'))
print(is_permmutation('hot', 'god'))
