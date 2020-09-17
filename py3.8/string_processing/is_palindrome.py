s = 'Was it a cat I saw?'

s = ''.join([i for i in s if i.isalpha()]).replace(' ', '').lower()


def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False

        i += 1
        j -= 1
    return True


print(is_palindrome(s))
