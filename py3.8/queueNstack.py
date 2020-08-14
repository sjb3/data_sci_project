# queue: first IN first OUT
# stack first IN last OUT

# Palindrome
# pre-process given strings
from collections import deque
s = 'cba4abc'
str = ''.join([i for i in s if i.isalpha()]).replace(' ', '').lower()
# print(str)
# print(str == str[:: -1])

# OR


def isPalindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True
# OR
# use deque package


class Solution:
    def __init__(self):
        self.stack = list()
        self.queue = deque()

    def pushCharacter(self, character):
        self.stack.append(character)

    def enqueCharacter(self, character):
        self.queue.append(character)

    def popCharacter(self):
        return self.stack.pop()

    def dequeCharacter(self):
        return self.queue.popleft()


s = input()
obj = Soluition()
l = len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueCharacter(s[i])

isPalindrome = True

for i in range(l//2):
    if obj.popCharacter[i] != obj.dequeCharacter[i]:
        isPalindrome = False
        break


print(isPalindrome('redcar'))
print(isPalindrome('whatever'))
print(isPalindrome('cba4abc'))
