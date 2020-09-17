'''
To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

1st: 1 is read off as "one 1" or 11.
2nd: 11 is read off as "two 1s" or 21.
3rd: 21 is read off as "one 2, then one 1" or 1211.
4th: 1211 is read off as "one 1, one 2, then two 1s" or 111221.
5th: 111221 is read off as "three 1s, two 2s, then one 1" or 312211.

'''


def next_num(s):
    result = []
    i = 0

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1

        result.append(str(count) + s[i])
        i += 1

    return ''.join(result)


print(next_num('1211'))

s = '1'
n = 4
for i in range(n):
    s = next_num(s)
    print(s)
