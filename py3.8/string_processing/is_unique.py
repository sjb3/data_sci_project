unique_str = 'asDFGljk'
non_unique_str = 'Non Unique String'


def is_unique(s):
    s = s.replace(' ', '').lower()

    ht = dict()
    for i in s:
        if i in ht:
            return False
        else:
            ht[i] = 1
    return True


print(is_unique(unique_str))
