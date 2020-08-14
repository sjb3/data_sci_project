# Algorithms in Python: Recursion -- Find Uppercase Letter in String

input1 = 'LucidDream'
input2 = 'lucidDream'
input3 = 'lUCidDream'


def find_upper(str):
    for i in range(len(str)):
        if str[i].isupper():
            return str[i]
    return None


def find_upper_recur(str, i=0):
    if str[i].isupper():
        return str[i]

    if i == len(str) - 1:
        return None

    return find_upper_recur(str, i+1)


print(find_upper(input1))
print(find_upper(input2))
print(find_upper(input3))

print(find_upper_recur(input1))
print(find_upper_recur(input2))
print(find_upper_recur(input3))
