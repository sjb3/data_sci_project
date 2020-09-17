'''
We will be considering how to determine
if a string is a palindrome permutation. Specifically:
Given a string, we wish to write a function to determine
if it is a permutation of a palindrome.

'''

word = 'taco cat'


def is_palin_perm(word):
    ht = dict()
    word = word.replace(' ', '').lower()

    for s in word:
        if s in ht:
            ht[s] += 1
        else:
            ht[s] = 1

    odd_count = 0
    for k, v in ht.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False

    return True


print(is_palin_perm('tacocat'))
