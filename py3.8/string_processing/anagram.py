# String Processing in Python: Is Anagram

s1 = 'fairy tales'
s2 = 'rail safety'

# normalize
s1 = s1.replace(' ', '').lower()
s2 = s2.replace(' ', '').lower()
# n log n time
# print(sorted(s1) == sorted(s2))


def is_anagram(s1, s2):
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False

    return True


print(is_anagram(s1, s2))
